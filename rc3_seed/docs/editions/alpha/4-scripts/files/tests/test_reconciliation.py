import sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT))
from capybara.connectors.mock import MockConnector
from capybara.services.reconciliation import compare_source_to_operational

class FakeFeature:
    def __init__(self,attrs): self.attributes=attrs

class Tests(unittest.TestCase):
    def test_detects_missing_and_drift(self):
        c=MockConnector(ROOT.parent/"sample_data")
        tickets=list(c.iter_tickets(limit=2))
        operational=[FakeFeature({"ITSM_ID":"T001","STATUS":"Closed"})]
        issues=compare_source_to_operational(tickets,operational)
        kinds={x.issue for x in issues}
        self.assertIn("Status drift",kinds)
        self.assertIn("Missing from ArcGIS operational layer",kinds)

if __name__=="__main__":
    unittest.main()
