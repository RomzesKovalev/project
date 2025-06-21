import unittest
from project.src.history_saver import save_history
import pandas as pd
import os
import logging

logger = logging.getLogger(__name__)

class TestHistorySaver(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_history.csv'
        self.data = {
            'cpu': [10.0, 20.0, 30.0],
            'memory': [20.0, 30.0, 40.0],
            'disk': [30.0, 40.0, 50.0]
        }

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_history(self):
        try:
            save_history(self.data, self.filename)
            logger.info(f"Tested save_history: {self.filename}")
            self.assertTrue(os.path.exists(self.filename), f"{self.filename} should exist")
            df = pd.read_csv(self.filename)
            self.assertEqual(len(df), 3, "DataFrame should have 3 rows")
            self.assertIn('cpu', df.columns, "DataFrame should have 'cpu' column")
            self.assertIn('memory', df.columns, "DataFrame should have 'memory' column")
            self.assertIn('disk', df.columns, "DataFrame should have 'disk' column")
            self.assertEqual(df['cpu'].tolist(), self.data['cpu'], "CPU values should match")
            self.assertEqual(df['memory'].tolist(), self.data['memory'], "Memory values should match")
            self.assertEqual(df['disk'].tolist(), self.data['disk'], "Disk values should match")

        except Exception as e:
            logger.error(f"Error testing save_history: {e}")
            self.fail(f"Failed to save history: {e}")

if __name__ == '__main__':
    unittest.main()
