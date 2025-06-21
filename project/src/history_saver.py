import pandas as pd
import logging

logger = logging.getLogger(__name__)

def save_history(data, filename='history.csv'):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        logger.info(f"History saved to {filename}")
    except Exception as e:
        logger.error(f"Error saving history to {filename}: {e}")