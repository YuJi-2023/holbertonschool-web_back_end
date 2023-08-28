#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""
from typing import Tuple
from typing import Union

v = Union[int, float]


def to_kv(k: str, v: float) -> Tuple:
    """function takes string k and mixed type v, return as a tuple"""
    first = k
    second = v ** 2
    result = (first, second)
    return result
