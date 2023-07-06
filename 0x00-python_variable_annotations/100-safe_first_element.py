#!/usr/bin/env python3
"""_summary_
"""
from typing import Sequence, Any, Union, NewType


NoneType = NewType('NoneType', None)


def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    """
    Retrieves the first element of a sequence

    Args:
        lst (Sequence[Any]): Sequence of Any element param

    Returns:
        Union[Any, NoneType]: return type
    """
    if lst:
        return lst[0]
    else:
        return None
