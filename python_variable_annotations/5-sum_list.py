#!/usr/bin/env python3
"""type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """sum_list function takes a float list and return sum as a float"""
    result = 0.0
    for i in input_list:
        result += i
    return result
