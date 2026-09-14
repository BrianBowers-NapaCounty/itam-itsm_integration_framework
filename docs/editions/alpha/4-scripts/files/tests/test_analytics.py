import sys,unittest,tempfile
from pathlib import Path
from datetime import datetime,timezone
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))

from capybara.analytics.windows import named_window,common_windows
from capybara.analytics.store import SQLiteAnalyticsStore
from capybara.analytics.aggregation import robust_anomalies,data_quality_row
from capybara.analytics.metrics import all_metrics
from capybara.connectors.mock import MockConnector

class Tests(unittest.TestCase):
    def setUp(self):
        self.c=MockConnector(ROOT.parent/"sample_data")
        self.t=list(self.c.iter_tickets());self.a=list(self.c.iter_assets())

    def test_windows(self):
        now=datetime(2026,9,13,12,0,tzinfo=timezone.utc)
        self.assertLess(named_window("3-month",now=now).start,now)
        self.assertGreaterEqual(len(common_windows(now=now)),10)

    def test_sqlite_store(self):
        with tempfile.TemporaryDirectory() as td:
            s=SQLiteAnalyticsStore(Path(td)/"x.sqlite")
            r=s.add_rows("Metric_Snapshots",[{"OBSERVED_UTC":datetime.now(timezone.utc),
                "PERIOD_CODE":"snapshot","METRIC_CODE":"tickets.active","METRIC_VALUE":3.0,
                "DIMENSION":"all","DIM_VALUE":"all"}])
            self.assertEqual(r["submitted"],1)
            self.assertEqual(len(s.query_rows("Metric_Snapshots")),1)

    def test_metrics(self):
        rows=all_metrics(tickets=self.t,assets=self.a,known_locations={"FIN-2-201"})
        self.assertTrue(any(x["metric_code"]=="assets.missing" for x in rows))

    def test_quality(self):
        row=data_quality_row(self.t,known_locations={"FIN-2-201","ADM-1-114"})
        self.assertGreaterEqual(row["SCORE"],0)
        self.assertLessEqual(row["SCORE"],1)

    def test_anomaly(self):
        pts=list(enumerate([10,11,10,9,10,11,60,10,9,11]))
        self.assertTrue(robust_anomalies(pts))

if __name__=="__main__":unittest.main()
