#!/usr/bin/env python3
"""simple pagination"""
import csv
import math
from typing import List, Dict, Union, Any


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
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

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

    def get_hyper(self, page: int = 1, page_size: int = 10)\
            -> Dict[str, Union[int, List[Any], None]]:
        """return a dictionary containing infos in key-value pairs"""
        data_list = self.dataset()
        return_list = self.get_page(page, page_size)

        if len(data_list) % page_size != 0:
            t_p = int(len(data_list) / page_size) + 1
        else:
            t_p = int(len(data_list) / page_size)

        n_p = page + 1
        if page >= t_p:
            n_p = None
        p_p = page - 1
        if p_p < 1:
            p_p = None

        info_dict = {
                "page_size": page_size,
                "page": page,
                "data": return_list,
                "next_page": n_p,
                "prev_page": p_p,
                "tatal_pages": t_p
                }
        return info_dict
