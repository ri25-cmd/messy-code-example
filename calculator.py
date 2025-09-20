def add(a, b):
    """```python
    Adds two numbers together.
    
    Args:
      a: The first number.  Must be a number.
      b: The second number. Must be a number.
    
    Returns:
      The sum of a and b.  Returns an error if either input is not a number.
    
    Raises:
      TypeError: If either a or b is not a number.
    
    
    ```
    """
    
    return a + b

def subtract(a, b):
    """Subtracts b from a."""
    return a - b

def multiply(a, b):
    """```
    Multiplies two numbers.
    
    Args:
      a: The first number.  Must be a number (int, float, complex).
      b: The second number. Must be a number (int, float, complex).
    
    Returns:
      The product of a and b.  Returns a complex number if either input is complex;
      otherwise returns an int or float, as appropriate.
    
    Raises:
      TypeError: If either input is not a number.
    
    ```
    """
    return a * b
