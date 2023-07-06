#!/usr/bin/env python3
"""
More on type annotation
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any,
    default: Union[T, None]
) -> Union[Any, T]:
    """
    functio to safetly get value from a dict using a given key

    Args:
        dct (Mapping): _description_
        key (Any): _description_
        default (Union[T, None]): _description_

    Returns:
        Union[Any, T]: _description_
    """

    if key in dct:
        return dct[key]
    else:
        return default
