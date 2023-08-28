#!/usr/bin/env python3
"""type-annotated function sum_mixed_list"""
from typing import Tuple
from typing import Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function takes string k and mixed type v, return as a tuple"""
    first: str = k
    second: float = v ** 2
    result = (first, second)
    return result
