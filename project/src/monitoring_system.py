import time
from data_collector import collect_cpu_usage, collect_memory_usage, collect_disk_usage
from graph_builder import plot_real_time
from notifier import send_system_notification
from history_saver import save_history
from report_exporter import export_report
import logging
import threading

# Настройка логирования
from logger import setup_logger
setup_logger()

logger = logging.getLogger(__name__)

def main():
    cpu_data = []
    memory_data = []
    disk_data = []

    # Запуск графика в отдельном потоке
    plot_thread = threading.Thread(target=plot_real_time)
    plot_thread.daemon = True
    plot_thread.start()

    try:
        while True:
            cpu_usage = collect_cpu_usage()
            memory_usage = collect_memory_usage()
            disk_usage = collect_disk_usage()

            if cpu_usage is not None:
                cpu_data.append(cpu_usage)
            if memory_usage is not None:
                memory_data.append(memory_usage)
            if disk_usage is not None:
                disk_data.append(disk_usage)

            if cpu_usage is not None:
                logger.info(f'Collected data - CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%')

            if cpu_usage is not None and cpu_usage > 65:
                send_system_notification('High CPU Usage', f'CPU usage is at {cpu_usage}%')

            time.sleep(0.5)  # Сбор данных каждые 0.5 секунды

    except KeyboardInterrupt:
        logger.info('Monitoring stopped by user')

    finally:
        save_history({
            'cpu': cpu_data,
            'memory': memory_data,
            'disk': disk_data
        })

        export_report({
            'cpu': cpu_data,
            'memory': memory_data,
            'disk': disk_data
        })

if __name__ == '__main__':
    main()