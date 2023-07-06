#!/usr/bin/env python3
"""
to_kv type annotaion file
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    a type-annotated function to_kv that takes a string k and an
    int OR float v as arguments and returns a tuple.

    Args:
        k (str): The first element of the tuple is the string
        v (Union[int, float]): The second element is the square of
        the int/float

    Returns:
        Tuple[str, float]: return type
    """

    return (k, v**2)
