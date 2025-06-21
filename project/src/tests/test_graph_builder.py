import unittest
from project.src.graph_builder import RealTimePlotter
import logging

logger = logging.getLogger(__name__)

class TestGraphBuilder(unittest.TestCase):
    def setUp(self):
        self.plotter = RealTimePlotter(interval=100, max_points=5)  # Короткий интервал для тестирования

    def test_update_plot(self):
        # Добавляем данные
        self.plotter.update_plot(None)
        self.plotter.update_plot(None)
        self.plotter.update_plot(None)
        self.plotter.update_plot(None)
        self.plotter.update_plot(None)

        # Проверяем, что данные добавлены корректно
        self.assertEqual(len(self.plotter.x_data), 5, "x_data should have 5 points")
        self.assertEqual(len(self.plotter.cpu_y_data), 5, "cpu_y_data should have 5 points")
        self.assertEqual(len(self.plotter.memory_y_data), 5, "memory_y_data should have 5 points")
        self.assertEqual(len(self.plotter.disk_y_data), 5, "disk_y_data should have 5 points")

        logger.info("Tested update_plot with 5 points")

        # Добавляем ещё одну точку и проверяем ограничение на максимальное количество точек
        self.plotter.update_plot(None)
        self.assertEqual(len(self.plotter.x_data), 5, "x_data should still have 5 points after adding one more")
        self.assertEqual(len(self.plotter.cpu_y_data), 5, "cpu_y_data should still have 5 points after adding one more")
        self.assertEqual(len(self.plotter.memory_y_data), 5, "memory_y_data should still have 5 points after adding one more")
        self.assertEqual(len(self.plotter.disk_y_data), 5, "disk_y_data should still have 5 points after adding one more")

        logger.info("Tested update_plot with max_points constraint")

if __name__ == '__main__':
    unittest.main()