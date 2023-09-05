#!/usr/bin/env python3
"""python helper function for pagination"""


def index_range(page, page_size):
    """return a tuple containing a start index and an end index"""
    start = int(page_size * (page - 1))
    end = int(page * page_size)
    result = (start, end)
    return result
