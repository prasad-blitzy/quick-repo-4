from typing import Union
import math

def add(a, b):
    return a + b

def add3(a, b, c):
    return a + b + c

def robust_add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Perform robust addition of two numeric values with comprehensive validation.
    
    This function adds two numbers together with extensive input validation including
    None checking, type validation, and special float value handling (NaN). It ensures
    that only valid numeric inputs are processed and provides clear error messages for
    invalid inputs.
    
    Args:
        a (Union[int, float]): The first numeric value to add. Must be an integer or float.
        b (Union[int, float]): The second numeric value to add. Must be an integer or float.
    
    Returns:
        Union[int, float]: The sum of a and b. Returns int if both inputs are int,
                          otherwise returns float.
    
    Raises:
        TypeError: If either parameter is None or not a numeric type (int or float).
        ValueError: If either parameter is NaN (Not a Number).
    
    Examples:
        >>> robust_add(5, 3)
        8
        >>> robust_add(2.5, 3.7)
        6.2
        >>> robust_add(10, 5.5)
        15.5
    """
    # Validation Layer 1 - None checking
    if a is None:
        raise TypeError("Parameter 'a' cannot be None. Expected numeric value (int or float).")
    if b is None:
        raise TypeError("Parameter 'b' cannot be None. Expected numeric value (int or float).")
    
    # Validation Layer 2 - Type checking
    if not isinstance(a, (int, float)):
        raise TypeError(f"Parameter 'a' must be a numeric type (int or float), got {type(a)}.")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Parameter 'b' must be a numeric type (int or float), got {type(b)}.")
    
    # Validation Layer 3 - NaN validation
    # Note: isinstance check above ensures we can safely call isnan on float values
    # For int values, we need to handle the case where isnan might not work
    try:
        if math.isnan(a):
            raise ValueError("Parameter 'a' cannot be NaN. Expected a valid numeric value.")
    except TypeError:
        # isnan raises TypeError for int, which is fine - integers cannot be NaN
        pass
    
    try:
        if math.isnan(b):
            raise ValueError("Parameter 'b' cannot be NaN. Expected a valid numeric value.")
    except TypeError:
        # isnan raises TypeError for int, which is fine - integers cannot be NaN
        pass
    
    # Computation - perform addition only after all validations pass
    result = a + b
    
    return result

def product(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Perform robust multiplication of two numeric values with comprehensive validation.
    
    This function multiplies two numbers together with extensive input validation including
    None checking, type validation, and special float value handling (NaN). It ensures
    that only valid numeric inputs are processed and provides clear error messages for
    invalid inputs. If either number is zero, the result will be zero.
    
    Args:
        a (Union[int, float]): The first numeric value to multiply. Must be an integer or float.
        b (Union[int, float]): The second numeric value to multiply. Must be an integer or float.
    
    Returns:
        Union[int, float]: The product of a and b. Returns int if both inputs are int,
                          otherwise returns float. Returns 0 if either input is 0.
    
    Raises:
        TypeError: If either parameter is None or not a numeric type (int or float).
        ValueError: If either parameter is NaN (Not a Number).
    
    Examples:
        >>> product(5, 3)
        15
        >>> product(2.5, 4)
        10.0
        >>> product(10, 0)
        0
        >>> product(0, 5.5)
        0
    """
    # Validation Layer 1 - None checking
    if a is None:
        raise TypeError("Parameter 'a' cannot be None. Expected numeric value (int or float).")
    if b is None:
        raise TypeError("Parameter 'b' cannot be None. Expected numeric value (int or float).")
    
    # Validation Layer 2 - Type checking
    if not isinstance(a, (int, float)):
        raise TypeError(f"Parameter 'a' must be a numeric type (int or float), got {type(a)}.")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Parameter 'b' must be a numeric type (int or float), got {type(b)}.")
    
    # Validation Layer 3 - NaN validation
    # Note: isinstance check above ensures we can safely call isnan on float values
    # For int values, we need to handle the case where isnan might not work
    try:
        if math.isnan(a):
            raise ValueError("Parameter 'a' cannot be NaN. Expected a valid numeric value.")
    except TypeError:
        # isnan raises TypeError for int, which is fine - integers cannot be NaN
        pass
    
    try:
        if math.isnan(b):
            raise ValueError("Parameter 'b' cannot be NaN. Expected a valid numeric value.")
    except TypeError:
        # isnan raises TypeError for int, which is fine - integers cannot be NaN
        pass
    
    # Computation - perform multiplication only after all validations pass
    # If either number is 0, the result will be 0 (mathematically correct)
    result = a * b
    
    return result
