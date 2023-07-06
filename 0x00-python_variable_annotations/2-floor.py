#!/usr/bin/env python3
"""
floor.py file
"""

from math import floor as math_floor


def floor(n: float) -> int:
    """
    a type-annotated function floor which takes
    a float n as argument and returns the floor of the float.

    Args:
        n (float): float argument

    Returns:
        int: int output
    """

    return math_floor(n)
