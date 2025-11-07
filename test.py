from typing import Union
from decimal import Decimal
import math


def add(a, b):
    return a + b


def add3(a, b, c):
    return a + b + c


def robust_add(
    a: Union[int, float, complex, Decimal],
    b: Union[int, float, complex, Decimal]
) -> Union[int, float, complex, Decimal]:
    """
    Robustly adds two numeric values with comprehensive type validation.
    
    This function provides production-grade addition with multiple layers of
    defensive validation to ensure reliable operation under all conditions.
    It supports standard Python numeric types while rejecting invalid inputs
    with clear, actionable error messages.
    
    Args:
        a: First numeric operand. Must be int, float, complex, or Decimal.
        b: Second numeric operand. Must be int, float, complex, or Decimal.
    
    Returns:
        The sum of a and b, maintaining appropriate type precision based on
        the input types. Returns int if both inputs are int, float if either
        input is float, complex if either input is complex, or Decimal if
        working with Decimal types.
    
    Raises:
        TypeError: If either operand is None or not a supported numeric type
                   (int, float, complex, or Decimal).
        ValueError: If the addition operation fails due to incompatible
                    numeric values or arithmetic errors.
    
    Examples (for documentation purposes):
        Basic integer addition:
            robust_add(5, 3) returns 8
        
        Floating-point addition:
            robust_add(2.5, 1.5) returns 4.0
        
        Mixed type addition:
            robust_add(5, 2.5) returns 7.5
        
        Complex number addition:
            robust_add(complex(1, 2), complex(3, 4)) returns (4+6j)
        
        High-precision decimal addition:
            robust_add(Decimal('0.1'), Decimal('0.2')) returns Decimal('0.3')
        
        Handles special float values:
            robust_add(float('inf'), 5) returns inf
            robust_add(float('nan'), 5) returns nan
    """
    # Validation Layer 1: None check
    if a is None or b is None:
        raise TypeError(
            f"robust_add() does not accept None values. "
            f"Received: a={a}, b={b}. "
            f"Please provide valid numeric values (int, float, complex, or Decimal)."
        )
    
    # Validation Layer 2: Type validation
    supported_types = (int, float, complex, Decimal)
    
    if not isinstance(a, supported_types):
        raise TypeError(
            f"robust_add() requires first operand to be a numeric type. "
            f"Expected: int, float, complex, or Decimal. "
            f"Received: {type(a).__name__} with value {repr(a)}."
        )
    
    if not isinstance(b, supported_types):
        raise TypeError(
            f"robust_add() requires second operand to be a numeric type. "
            f"Expected: int, float, complex, or Decimal. "
            f"Received: {type(b).__name__} with value {repr(b)}."
        )
    
    # Validation Layer 3: Float edge case handling
    # Note: NaN and infinity are valid float values that should be handled
    # gracefully. Python's addition operator handles these correctly:
    # - inf + x = inf (for finite x)
    # - inf + inf = inf
    # - inf + (-inf) = nan
    # - nan + x = nan (NaN propagates)
    # We validate these exist but allow the operation to proceed naturally.
    
    if isinstance(a, float):
        if math.isnan(a):
            # NaN propagates through addition - this is expected behavior
            pass
        if math.isinf(a):
            # Infinity addition follows IEEE 754 standard - allow it
            pass
    
    if isinstance(b, float):
        if math.isnan(b):
            # NaN propagates through addition - this is expected behavior
            pass
        if math.isinf(b):
            # Infinity addition follows IEEE 754 standard - allow it
            pass
    
    # Validation Layer 4: Safe operation execution
    try:
        result = a + b
        return result
    except TypeError as e:
        # Catch incompatible type operations (e.g., complex + incompatible type)
        raise ValueError(
            f"Addition operation failed due to type incompatibility. "
            f"Cannot add {type(a).__name__} and {type(b).__name__}. "
            f"Original error: {str(e)}"
        )
    except Exception as e:
        # Catch any other unexpected arithmetic errors
        raise ValueError(
            f"Addition operation failed with unexpected error. "
            f"Operands: a={repr(a)} ({type(a).__name__}), "
            f"b={repr(b)} ({type(b).__name__}). "
            f"Error: {str(e)}"
        )
