import logging
import datetime


from mercado_bitcoin.ingestors import AwsDaySummaryIngestor
from mercado_bitcoin.writers import S3Writer


def lambda_handler(event, context):
    logging.info(f"event received: {event}")

    AwsDaySummaryIngestor(
        writer=S3Writer,
        coins=["BTC", "ETH", "LTC", "BCH"],
        default_start_date=datetime.date(2021, 3, 1),
    ).ingest()
