import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from data_collector import collect_cpu_usage, collect_memory_usage, collect_disk_usage
import logging

logger = logging.getLogger(__name__)

class RealTimePlotter:
    def __init__(self, interval=500, max_points=100):
        self.fig, self.ax = plt.subplots(3, 1, figsize=(10, 12), sharex=True)
        self.cpu_line, = self.ax[0].plot([], [], label='CPU Usage (%)')
        self.memory_line, = self.ax[1].plot([], [], label='Memory Usage (%)')
        self.disk_line, = self.ax[2].plot([], [], label='Disk Usage (%)')

        self.ax[0].set_title('CPU Usage Over Time')
        self.ax[1].set_title('Memory Usage Over Time')
        self.ax[2].set_title('Disk Usage Over Time')

        for ax in self.ax:
            ax.set_xlabel('Time')
            ax.set_ylabel('Usage (%)')
            ax.legend()
            ax.set_ylim(0, 100)

        self.x_data = []
        self.cpu_y_data = []
        self.memory_y_data = []
        self.disk_y_data = []

        self.max_points = max_points
        self.interval = interval

    def update_plot(self, frame):
        try:
            cpu_usage = collect_cpu_usage()
            memory_usage = collect_memory_usage()
            disk_usage = collect_disk_usage()

            if cpu_usage is not None:
                self.cpu_y_data.append(cpu_usage)
            if memory_usage is not None:
                self.memory_y_data.append(memory_usage)
            if disk_usage is not None:
                self.disk_y_data.append(disk_usage)

            self.x_data.append(len(self.cpu_y_data))

            if len(self.x_data) > self.max_points:
                self.x_data.pop(0)
                self.cpu_y_data.pop(0)
                self.memory_y_data.pop(0)
                self.disk_y_data.pop(0)

            self.cpu_line.set_data(self.x_data, self.cpu_y_data)
            self.memory_line.set_data(self.x_data, self.memory_y_data)
            self.disk_line.set_data(self.x_data, self.disk_y_data)

            for ax in self.ax:
                ax.relim()
                ax.autoscale_view()

            logger.info(f'Updated plot with CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%')
        except Exception as e:
            logger.error(f"Error updating plot: {e}")

    def start_animation(self):
        ani = FuncAnimation(self.fig, self.update_plot, interval=self.interval, blit=False, cache_frame_data=False)
        plt.tight_layout()
        plt.show()

def plot_real_time():
    plotter = RealTimePlotter()
    plotter.start_animation()
