#!/usr/bin/env python3
"""simple pagination project """
import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """returns a tuple containing the start and end index of a page """
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
        """gets the page number and page size, returns the data from dataset
        of the specified page number """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        page_range = index_range(page, page_size)
        start, end = page_range
        data_list = self.dataset()
        return data_list[start: end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """returns a dictionary containing information on a page of data
        from dataset """
        data_list = self.dataset()
        return_list = self.get_page(page, page_size)
        total_p = math.ceil(len(data_list) / page_size)
        next_p = page + 1
        if next_p > total_p:
            next_p = None
        prev_p = page - 1
        if prev_p < 1:
            prev_p = None
        info_dict = {
            "page_size": page_size,
            "page": page,
            "data": return_list,
            "next_page": next_p,
            "prev_page": prev_p, "total_pages": total_p
        }
        return info_dict
