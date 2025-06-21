import unittest
from project.src.notifier import send_console_notification, send_system_notification
import logging

logger = logging.getLogger(__name__)

class TestNotifier(unittest.TestCase):
    def test_send_console_notification(self):
        try:
            send_console_notification("Test Console Notification")
            logger.info("Tested send_console_notification successfully")
        except Exception as e:
            logger.error(f"Error testing send_console_notification: {e}")
            self.fail(f"Failed to send console notification: {e}")

    def test_send_system_notification(self):
        try:
            send_system_notification("Test System Notification", "This is a test notification")
            logger.info("Tested send_system_notification successfully")
        except Exception as e:
            logger.error(f"Error testing send_system_notification: {e}")
            self.fail(f"Failed to send system notification: {e}")

if __name__ == '__main__':
    unittest.main()