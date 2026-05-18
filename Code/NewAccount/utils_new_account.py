# Python library
import re

# My Path
from config import CLIENTS_PATH, EMPLOYEES_PATH, REGEX_EMAIL, REGEX_NIF, REGEX_PHONE

# My Library
from GenericUtlis.files import (
    check_file,
    read_json,
    write_json,
)


# Save account in the database
def save_account(client: dict, path: str) -> None:

    check_file(path)

    new_data = read_json(path)
    new_data["next_id"] += 1

    if path == CLIENTS_PATH:
        new_data["clients"].append(client)

    elif path == EMPLOYEES_PATH:
        new_data["employees"].append(client)

    write_json(path, new_data)
