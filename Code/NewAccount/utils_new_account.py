# Python library
import re

# Regex code
# My Path
from config import CLIENTS_PATH, REGEX_EMAIL, REGEX_PHONE

# My Library
from GenericUtlis.files import create_json, read_json


# Save account in the database
def save_account(client: dict):
    data = read_json(CLIENTS_PATH)

    id = len(data["clients"]) + 1

    client["id"] = id

    data["clients"].append(client)

    create_json(CLIENTS_PATH, data)


# Check if exists email
def check_email(clients: dict, email: str):
    for client in clients["clients"]:
        if client["email"] == email:
            return False

    return True


# Validate the email format
def validate_email(email: str) -> bool:
    if re.match(REGEX_EMAIL, email):
        return True

    return False


# Validate the phone format
def validate_phone(phone: str) -> bool:
    if re.match(REGEX_PHONE, phone):
        return True

    return False
