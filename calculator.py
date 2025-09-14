def add(a, b): # No docstring
    """```python
    Adds two numbers together.
    
    Args:
      a: The first number.  Must be a number type (int, float, complex).
      b: The second number. Must be a number type (int, float, complex).
    
    Returns:
      The sum of a and b.  Returns the same type as the inputs if both are of the same type. 
      If inputs are of different numeric types, returns a float.  Raises TypeError if 
      inputs are not numbers.
    
    Raises:
      TypeError: If either a or b is not a number.
    
    ```
    """
    return a + b

def subtract(a, b):
    """Subtracts b from a."""
    return a - b

def multiply(a, b): # No docstring
    """```
    Multiplies two numbers.
    
    Args:
      a: The first number.  Must be a number type (int or float).
      b: The second number. Must be a number type (int or float).
    
    Returns:
      The product of a and b.  Returns a float if either input is a float; otherwise returns an int.
    
    Raises:
      TypeError: If either input is not a number.
    
    ```
    """
    return a * b
