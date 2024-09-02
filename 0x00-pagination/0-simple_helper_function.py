#!/usr/bin/env python3
"""`index_range` module"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of size 2 containing a start index and an end index
    corresponding to the range of indexes
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
