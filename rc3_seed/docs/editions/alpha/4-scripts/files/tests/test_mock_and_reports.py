import sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from capybara.connectors.mock import MockConnector
from capybara.services.reporting import assignment_backlog,tickets_on_hold,service_hotspots
from capybara.services.notifications import missing_assets

class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.c=MockConnector(ROOT.parent/"sample_data")
        cls.t=list(cls.c.iter_tickets())
        cls.a=list(cls.c.iter_assets())

    def test_data(self):
        self.assertGreaterEqual(len(self.t),5)
        self.assertGreaterEqual(len(self.a),5)

    def test_reports(self):
        self.assertTrue(assignment_backlog(self.t))
        self.assertGreaterEqual(len(tickets_on_hold(self.t)),2)
        self.assertTrue(service_hotspots(self.t))

    def test_missing(self):
        self.assertEqual(len(missing_assets(self.a)),1)

if __name__=="__main__":
    unittest.main()
