from dataclasses import dataclass
import re

TAG_RE = re.compile(r"(?<!\\w)#(decision|evidence|risk|claim)\\b", re.I)

@dataclass(frozen=True)
class Event:
    kind: str
    line: int
    text: str

def extract(markdown: str) -> list[Event]:
    events: list[Event] = []
    for line_no, line in enumerate(markdown.splitlines(), start=1):
        for kind in [m.lower() for m in TAG_RE.findall(line)]:
            events.append(Event(kind, line_no, line.strip()))
    return events
