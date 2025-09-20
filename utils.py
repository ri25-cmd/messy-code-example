import json
from datetime import datetime, timedelta

# This function is already well-documented. The agent should ignore it.
def get_db_connection(connection_string: str):
    """
    Establishes a connection to the database.

    Args:
        connection_string (str): The connection string for the database.

    Returns:
        A database connection object.
    """
    print(f"Connecting to {connection_string}...")
    # Mock connection object
    return {"status": "connected"}

# --- AGENT TARGETS ---
# These functions are missing docstrings. The agent must find and fix them.

def process_user_data(user_data: dict, schema: list):
    """```
    Validates and processes user data according to a provided schema.
    
    Args:
      user_data: A dictionary containing user data.  Must be a dictionary; otherwise, a TypeError is raised.
      schema: A list of keys representing the required fields.  Only these keys from user_data will be included in the output.
    
    Returns:
      A new dictionary containing only the keys specified in the schema, plus a new "last_processed" key with the current UTC timestamp in ISO format.  Returns an empty dictionary if user_data is empty or contains no keys from the schema.
    
    Raises:
      TypeError: If user_data is not a dictionary.
    
    ```
    """
    if not isinstance(user_data, dict):
        raise TypeError("user_data must be a dictionary.")
    
    validated_data = {}
    for key in schema:
        validated_data[key] = user_data.get(key)
        
    validated_data["last_processed"] = datetime.utcnow().isoformat()
    return validated_data

def format_api_response(data, status_code: int = 200):
    """```python
    Formats API response data into a JSON string.
    
    Args:
      data: The data to be included in the response.  Can be any JSON serializable object.
      status_code: The HTTP status code. Defaults to 200 (OK).
    
    Returns:
      A tuple containing:
        - A JSON string representing the formatted response.  Includes an 'error' 
          key indicating success (False) or failure (True), and a 'data' key for 
          successful responses or 'details' for errors.
        - The HTTP status code.
    
    Raises:
      TypeError: If data is not JSON serializable.
    
    ```
    """
    if status_code >= 400:
        response_object = {"error": True, "details": data}
    else:
        response_object = {"error": False, "data": data}
        
    return json.dumps(response_object), status_code

