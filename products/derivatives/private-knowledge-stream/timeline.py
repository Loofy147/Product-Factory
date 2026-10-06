from dataclasses import dataclass
import re

TAG_RE = re.compile(r"(?:^|\s)#(decision|evidence|risk|claim)(?![A-Za-z0-9_])", re.I)

@dataclass(frozen=True)
class Event:
    kind: str
    line: int
    text: str

def extract(markdown: str) -> list[Event]:
    events: list[Event] = []
    for line_no, line in enumerate(markdown.splitlines(), start=1):
        for match in TAG_RE.finditer(line):
            events.append(Event(match.group(1).lower(), line_no, line.strip()))
    return events
