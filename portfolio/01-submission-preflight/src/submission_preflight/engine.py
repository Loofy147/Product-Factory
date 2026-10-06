from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path


@dataclass(frozen=True)
class Finding:
    requirement_id: str
    title: str
    status: str
    reason: str


@dataclass(frozen=True)
class PreflightReport:
    findings: list[Finding]
    manifest: list[dict[str, str | int]]

    @property
    def summary(self) -> dict[str, int]:
        result = {"PASS": 0, "FAIL": 0, "UNKNOWN": 0}
        for finding in self.findings:
            result[finding.status] += 1
        return result


def _sha256(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def run_preflight(requirements: list[dict], evidence_dir: Path) -> PreflightReport:
    if not evidence_dir.is_dir():
        raise ValueError(f"Evidence directory does not exist: {evidence_dir}")

    findings: list[Finding] = []
    manifest: list[dict[str, str | int]] = []

    for requirement in requirements:
        requirement_id = str(requirement["id"])
        title = str(requirement["title"])
        filename = str(requirement["filename"])
        expected_type = str(requirement.get("type", "")).lower().lstrip(".")
        required = bool(requirement.get("required", True))

        path = (evidence_dir / filename).resolve()
        evidence_root = evidence_dir.resolve()
        if path != evidence_root and evidence_root not in path.parents:
            raise ValueError(f"Invalid evidence path: {filename}")

        if not path.exists():
            status = "FAIL" if required else "UNKNOWN"
            reason = "MISSING_FILE" if required else "OPTIONAL_EVIDENCE_ABSENT"
            findings.append(Finding(requirement_id, title, status, reason))
            continue

        if not path.is_file():
            findings.append(Finding(requirement_id, title, "FAIL", "NOT_A_FILE"))
            continue

        actual_type = path.suffix.lower().lstrip(".")
        if expected_type and actual_type != expected_type:
            findings.append(Finding(requirement_id, title, "FAIL", "WRONG_TYPE"))
            continue

        manifest.append(
            {
                "requirement_id": requirement_id,
                "filename": filename,
                "size": path.stat().st_size,
                "sha256": _sha256(path),
            }
        )
        findings.append(Finding(requirement_id, title, "PASS", "FILE_PRESENT_AND_TYPED"))

    return PreflightReport(findings=findings, manifest=manifest)
