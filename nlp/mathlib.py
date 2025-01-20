# /workspaces/Managing_python_projects/nlp/mathlib.py

import math

def sqrt(value):
    if value < 0:
        raise ValueError("Cannot compute the square root of a negative number")
    return math.sqrt(value)
