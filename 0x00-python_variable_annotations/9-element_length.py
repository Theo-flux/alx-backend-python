#!/usr/bin/env python3
"""
ducktyping a function
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """_summary_

    Args:
        lst (Iterable[Sequence]): iterable sequence of arguments

    Returns:
        List[Tuple[Sequence, int]]: return value
    """
    return [(i, len(i)) for i in lst]
