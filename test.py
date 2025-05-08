from books_recommender.exception.exception_handler import AppException
##books_recommender\exception\exception_handler
import sys


try:
    a = 2/0
except Exception as e:
    raise AppException(e, sys) from e