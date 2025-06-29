def get_telemetry_data(api_url, params):
    import requests

    response = requests.get(api_url, params=params)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

def normalize_telemetry_data(raw_data):
    normalized_data = []
    for entry in raw_data:
        normalized_entry = {
            "service": entry.get("service"),
            "metric": entry.get("metric"),
            "value": entry.get("value"),
            "timestamp": entry.get("timestamp"),
        }
        normalized_data.append(normalized_entry)
    return normalized_data

def save_to_vector_db(data, vector_db_client):
    for entry in data:
        vector_db_client.index(entry)  # Assuming vector_db_client has an index method

def load_vector_db(vector_db_client):
    return vector_db_client.load_all()  # Assuming vector_db_client has a load_all method

def clean_up_data(data):
    return [entry for entry in data if entry.get("value") is not None]  # Remove entries with None values