#!/usr/bin/env python3
"""
make multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    type-annotated function make_multiplier that takes a float multiplier
    as argument and returns a function that multiplies a float by multiplier

    Args:
        multiplier (float): float argument

    Returns:
        Callable[[float], float]: function that accepts float argument
        and returns float
    """

    return lambda a: a * multiplier
