import psutil
import logging

logger = logging.getLogger(__name__)

def collect_cpu_usage():
    try:
        cpu_usage = psutil.cpu_percent(interval=0.5)
        logger.debug(f"Collected CPU usage: {cpu_usage}%")
        return cpu_usage
    except Exception as e:
        logger.error(f"Error collecting CPU usage: {e}")
        return None

def collect_memory_usage():
    try:
        memory = psutil.virtual_memory()
        memory_usage = memory.percent
        logger.debug(f"Collected Memory usage: {memory_usage}%")
        return memory_usage
    except Exception as e:
        logger.error(f"Error collecting memory usage: {e}")
        return None

def collect_disk_usage():
    try:
        partitions = psutil.disk_partitions()
        usages = []

        for part in partitions:
            if 'cdrom' in part.opts or part.fstype == '':
                continue
            try:
                usage = psutil.disk_usage(part.mountpoint).percent
                usages.append(usage)
                logger.debug(f"Disk {part.device} ({part.mountpoint}): {usage}%")
            except PermissionError:
                continue

        if usages:
            avg_usage = sum(usages) / len(usages)
            logger.debug(f"Average Disk usage: {avg_usage}%")
            return avg_usage
        else:
            logger.warning("No accessible disk partitions found.")
            return None
    except Exception as e:
        logger.error(f"Error collecting disk usage: {e}")
        return None