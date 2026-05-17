# Python library
import json
import os

# Path
from config import CLIENTS_PATH, EMPLOYEES_PATH


# Read json file
# Run a test; if there is an error,
# it will run two tests:
#   “file not found” or “error in JSON.”
def read_json(path: str):
    try:
        with open(path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return None

    except json.JSONDecodeError:
        return None


# Write json file
# Don't create a structure
def write_json(path: str, data: dict):
    with open(path, "w") as file:
        json.dump(data, file)


# Create the structure of JSON file
def create_json(path: str, data: dict):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    write_json(path, data)


# Check if the exists or not
def file_exists(path: str) -> bool:
    return os.path.isfile(path)


# Checks whether the file exists
def check_file(path: str) -> None:
    if not file_exists(path):
        if path == CLIENTS_PATH:
            create_json(path, {"next_id": 1, "clients": []})

            data = read_json(path)
            if data is None:
                create_json(path, {"next_id": 1, "clients": []})

        elif path == EMPLOYEES_PATH:
            create_json(path, {"next_id": 1, "employees": []})

            data = read_json(path)
            if data is None:
                create_json(path, {"next_id": 1, "employees": []})
