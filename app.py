
from books_recommender.exception.exception_handler import AppException
import sys
from books_recommender.logger.log import logging

try:
    a = 2/0
except Exception as e:

    logging.info()
    raise AppException(e, sys) from e