import math

def sqrt(value):
    """
    Calculate the square root of a given value.

    Args:
        value (float): The value to calculate the square root for.

    Returns:
        float: The square root of the value.

    Raises:
        ValueError: If the input value is negative.
    """
    if value < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return round(math.sqrt(value), 4)  # Round to 4 decimal places
