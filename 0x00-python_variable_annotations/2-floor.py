#!/usr/bin/env python3
""" Basic annotations floor """

import math


def floor(n: float) -> int:
    """ Returns  floor of the float """
    return math.floor(n)
print(floor(3.14) == math.floor(3.14))
print(floor.__annotations__)
