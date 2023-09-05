#!/usr/bin/env python3
"""simple pagination"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """return a tuple containing a start index and an end index"""
    start = int(page_size * (page - 1))
    end = int(page * page_size)
    result = (start, end)
    return result


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the list according to matched page"""
        assert all(isinstance(x, int) and x > 0 for x in (page, page_size))

        page_range = index_range(page, page_size)
        start_idx = page_range[0]
        end_idx = page_range[1]
        return_list = []
        data_list = self.dataset()
        i = start_idx

        if page * page_size > len(data_list):
            return return_list
        else:
            for i in range(start_idx, end_idx):
                return_list.append(data_list[i])
        return return_list
