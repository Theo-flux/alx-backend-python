#!/usr/bin/env python3
"""
sum_list function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    type-annotated function sum_list which takes
    a list input_list of floats as argument and returns their sum as a float.

    Args:
        input_list (List): list of float param

    Returns:
        float: output of float
    """
    num: float = 0.0

    for f in input_list:
        num = num + f

    return num
