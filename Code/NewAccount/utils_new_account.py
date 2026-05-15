# Python library
import re

# Regex code
# My Path
from config import CLIENTS_PATH, REGEX_EMAIL, REGEX_NIF, REGEX_PHONE

# My Library
from GenericUtlis.files import create_json, file_exists, read_json, write_json


# Save account in the database
def save_account(client: dict):

    check_clients_file()

    new_data = read_json(CLIENTS_PATH)
    new_data["next_id"] += 1
    new_data["clients"].append(client)

    write_json(CLIENTS_PATH, new_data)


# Checks whether the file exists
def check_clients_file():
    if not file_exists(CLIENTS_PATH):
        create_json(CLIENTS_PATH, {"next_id": 1, "clients": []})

    data = read_json(CLIENTS_PATH)
    if data is None:
        create_json(CLIENTS_PATH, {"next_id": 1, "clients": []})


# Check if exists email
def check_email(email: str) -> bool:

    check_clients_file()

    clients = read_json(CLIENTS_PATH)

    for client in clients["clients"]:
        if client["email"] == email:
            return False

    return True


# Check if exists phone
def check_phone(phone: str) -> bool:

    check_clients_file()

    clients = read_json(CLIENTS_PATH)
    for client in clients["clients"]:
        if client["phone"] == phone:
            return False

    return True


# Check if exists nif
def check_nif(nif: str) -> bool:

    check_clients_file()

    clients = read_json(CLIENTS_PATH)

    for client in clients["clients"]:
        if client["nif"] == nif:
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


# Validate age
def validate_age(age: int) -> bool:
    if age < 16 or age > 99:
        return False

    return True


# Validate the len of password
def validate_len_password(password: str) -> bool:
    if len(password) < 8:
        return False

    return True


# Validate the size of name
def validate_name(name: str) -> bool:
    if len(name) == 0:
        return False

    return True


def validate_nif(nif: str) -> bool:
    if re.match(REGEX_NIF, nif):
        return False

    return True
