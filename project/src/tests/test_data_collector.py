import unittest
from project.src.data_collector import collect_cpu_usage, collect_memory_usage, collect_disk_usage
import logging

logger = logging.getLogger(__name__)

class TestDataCollector(unittest.TestCase):
    def test_collect_cpu_usage(self):
        cpu_usage = collect_cpu_usage()
        self.assertIsNotNone(cpu_usage, "CPU usage should not be None")
        self.assertGreaterEqual(cpu_usage, 0, "CPU usage should be >= 0")
        self.assertLessEqual(cpu_usage, 100, "CPU usage should be <= 100")
        logger.info(f"Tested collect_cpu_usage: {cpu_usage}%")

    def test_collect_memory_usage(self):
        memory_usage = collect_memory_usage()
        self.assertIsNotNone(memory_usage, "Memory usage should not be None")
        self.assertGreaterEqual(memory_usage, 0, "Memory usage should be >= 0")
        self.assertLessEqual(memory_usage, 100, "Memory usage should be <= 100")
        logger.info(f"Tested collect_memory_usage: {memory_usage}%")

    def test_collect_disk_usage(self):
        disk_usage = collect_disk_usage()
        self.assertIsNotNone(disk_usage, "Disk usage should not be None")
        self.assertGreaterEqual(disk_usage, 0, "Disk usage should be >= 0")
        self.assertLessEqual(disk_usage, 100, "Disk usage should be <= 100")
        logger.info(f"Tested collect_disk_usage: {disk_usage}%")

if __name__ == '__main__':
    unittest.main()