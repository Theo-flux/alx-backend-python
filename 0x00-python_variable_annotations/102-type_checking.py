#!/usr/bin/env python3
"""_summary_
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    """
    creates multiple copies of element in a tuple by a factor

    Args:
        lst (Tuple): _description_
        factor (int, optional): _description_. Defaults to 2.

    Returns:
        Tuple: _description_
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)

# if __name__ == '__main__':
#     print(zoom_3x)
