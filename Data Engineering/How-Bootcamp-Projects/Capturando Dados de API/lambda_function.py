import datetime
from ingestors import AwsDaySummaryIngestor
from writers import S3Writter
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

def lambda_handler(event, context):
    logger.info(f"{event}")
    logger.info(f"{context}")
