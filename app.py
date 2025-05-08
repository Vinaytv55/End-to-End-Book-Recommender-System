
from books_recommender.exception.exception_handler import AppException
import sys

try:
    a = 2/0
except Exception as e:
    raise AppException(e, sys) from e