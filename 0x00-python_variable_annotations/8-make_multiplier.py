#!/usr/bin/env python3
"""Contains a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """use callble function to use multiplier
    """

    def multiplier_func(number: float) -> float:
        """multi * num"""
        return multiplier * number

    return multiplier_func
