#!/usr/bin/env python3
"""add type-annotation for function element_length"""
from typing import List
from typing import Tuple
from typing import Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """function takes an iterator and returns a list of tuple
    containing the element and its length"""
    return [(i, len(i)) for i in lst]
