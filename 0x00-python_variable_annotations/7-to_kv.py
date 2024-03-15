#!/usr/bin/env python3
""" string and int/float to tuple"""
from typing import Callable, Iterator, Union, Optional, List, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
     k and an int OR float v as arguments
    returns a tuple.
    """

    return (k, v**2)
print(to_kv.__annotations__)
print(to_kv("eggs", 3))
print(to_kv("school", 0.02))
