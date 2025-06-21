import logging
from plyer import notification

logger = logging.getLogger(__name__)

def send_console_notification(message):
    try:
        print(f"Notification: {message}")
        logger.info(f"Console notification sent: {message}")
    except Exception as e:
        logger.error(f"Error sending console notification: {e}")

def send_system_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="Monitoring System",
            timeout=10
        )
        logger.info(f"System notification sent: {title} - {message}")
    except Exception as e:
        logger.error(f"Error sending system notification: {e}")