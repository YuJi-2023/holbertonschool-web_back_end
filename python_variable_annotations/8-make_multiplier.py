#!/usr/bin/env python3
"""type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function takes a float and returns a function"""
    def f(x: float) -> float:
        """ return result of a float mutiplied by the given multiplier"""
        return x * multiplier
    return f
