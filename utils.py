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
    if not isinstance(user_data, dict):
        raise TypeError("user_data must be a dictionary.")
    
    validated_data = {}
    for key in schema:
        validated_data[key] = user_data.get(key)
        
    validated_data["last_processed"] = datetime.utcnow().isoformat()
    return validated_data

def format_api_response(data, status_code: int = 200):
    if status_code >= 400:
        response_object = {"error": True, "details": data}
    else:
        response_object = {"error": False, "data": data}
        
    return json.dumps(response_object), status_code

