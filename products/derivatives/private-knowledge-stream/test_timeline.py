from timeline import extract

def test_extracts_research_events():
    doc = "# Decision #decision\nEvidence #evidence A\nRisk #risk B\n"
    events = extract(doc)
    assert [e.kind for e in events] == ["decision", "evidence", "risk"]
    assert events[0].line == 1
