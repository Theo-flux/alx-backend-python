#!/usr/bin/env python3
"""
sum mixed list file
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    type-annotated function sum_mixed_list which takes a
    list mxd_lst of integers and floats and returns their sum as a float.

    Args:
        mxd_lst (List[Optional[int, float]]): a list of integers and
        floats as param

    Returns:
        float: a sinlge value of type float
    """
    num: Union[int, float] = 0.0

    for i in mxd_lst:
        num = num + i

    return num
