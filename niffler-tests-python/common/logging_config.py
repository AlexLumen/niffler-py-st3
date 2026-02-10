import logging

from common.project import config
from common.redacting_filter import RedactingFilter


def produce_logger(name):
    logger = logging.getLogger(name)
    filter = RedactingFilter(for_masking)
    logger.addFilter(filter)
    return logger


for_masking = [
    config.api_key,
    config.url
]
