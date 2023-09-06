#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """take two arguments index with default None and page_size with
        default 10, return a dictionary with key-value paris
        """
        full_list = self.dataset()
        indexed_list = self.indexed_dataset()
        assert index <= len(full_list)
        start_idx = index
        end_idx = index + page_size

        data_list = [indexed_list[i] for
                     i in range(start_idx, end_idx) if i in indexed_list]

        return_dict = {
            "index": index,
            "data": data_list,
            "page_size": page_size,
            "next_index": end_idx,
        }
        return return_dict
