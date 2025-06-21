import pandas as pd
import logging

logger = logging.getLogger(__name__)

def export_report(data, filename='report.csv'):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        logger.info(f"Report exported to {filename}")
    except Exception as e:
        logger.error(f"Error exporting report to {filename}: {e}")