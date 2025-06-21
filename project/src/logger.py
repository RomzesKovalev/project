import logging

def setup_logger():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        filename='app.log',
                        filemode='w')

setup_logger()