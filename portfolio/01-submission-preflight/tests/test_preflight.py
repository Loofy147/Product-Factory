from pathlib import Path

import pytest

from submission_preflight.engine import run_preflight


def test_required_present_file_passes(tmp_path: Path):
    evidence = tmp_path / "evidence"
    evidence.mkdir()
    (evidence / "01_bid_form.pdf").write_bytes(b"pdf-like content")

    report = run_preflight(
        [{
            "id": "REQ-001",
            "title": "Bid form",
            "required": True,
            "filename": "01_bid_form.pdf",
            "type": "pdf",
        }],
        evidence,
    )

    assert report.summary == {"PASS": 1, "FAIL": 0, "UNKNOWN": 0}
    assert report.findings[0].status == "PASS"
    assert report.findings[0].requirement_id == "REQ-001"
    assert report.manifest[0]["sha256"]


def test_required_missing_file_is_blocking(tmp_path: Path):
    evidence = tmp_path / "evidence"
    evidence.mkdir()

    report = run_preflight(
        [{
            "id": "REQ-002",
            "title": "Technical annex",
            "required": True,
            "filename": "10_technical_annex.pdf",
            "type": "pdf",
        }],
        evidence,
    )

    assert report.summary == {"PASS": 0, "FAIL": 1, "UNKNOWN": 0}
    assert report.findings[0].status == "FAIL"
    assert report.findings[0].reason == "MISSING_FILE"


def test_required_file_with_wrong_extension_fails(tmp_path: Path):
    evidence = tmp_path / "evidence"
    evidence.mkdir()
    (evidence / "01_bid_form.txt").write_text("wrong type", encoding="utf-8")

    report = run_preflight(
        [{
            "id": "REQ-003",
            "title": "Bid form",
            "required": True,
            "filename": "01_bid_form.txt",
            "type": "pdf",
        }],
        evidence,
    )

    assert report.summary == {"PASS": 0, "FAIL": 1, "UNKNOWN": 0}
    assert report.findings[0].reason == "WRONG_TYPE"


def test_optional_missing_file_is_unknown_not_failure(tmp_path: Path):
    evidence = tmp_path / "evidence"
    evidence.mkdir()

    report = run_preflight(
        [{
            "id": "REQ-004",
            "title": "Optional brochure",
            "required": False,
            "filename": "brochure.pdf",
            "type": "pdf",
        }],
        evidence,
    )

    assert report.summary == {"PASS": 0, "FAIL": 0, "UNKNOWN": 1}
    assert report.findings[0].status == "UNKNOWN"
    assert report.findings[0].reason == "OPTIONAL_EVIDENCE_ABSENT"


def test_evidence_filename_cannot_escape_evidence_directory(tmp_path: Path):
    evidence = tmp_path / "evidence"
    evidence.mkdir()
    outside = tmp_path / "outside.pdf"
    outside.write_bytes(b"must not be accepted")

    with pytest.raises(ValueError, match="Invalid evidence path"):
        run_preflight(
            [{
                "id": "REQ-005",
                "title": "Escaped file",
                "required": True,
                "filename": "../outside.pdf",
                "type": "pdf",
            }],
            evidence,
        )
