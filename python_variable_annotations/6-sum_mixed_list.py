#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""
from typing import List
from typing import Union

Num = Union[int, float]


def sum_mixed_list(mxd_lst: List[Num]) -> float:
    """function takes a mixed list and return sum as a float"""
    result = 0.0
    for i in mxd_lst:
        result += i
    return result
