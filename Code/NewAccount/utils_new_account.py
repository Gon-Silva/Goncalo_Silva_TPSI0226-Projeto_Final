# Python library
import re

# Regex code
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


# Check if exists email
def check_email(email: str) -> bool:

    check_file(CLIENTS_PATH)

    clients = read_json(CLIENTS_PATH)

    for client in clients["clients"]:
        if client["email"] == email:
            return False

    return True


# Check if exists phone
def check_phone(phone: str) -> bool:

    check_file(CLIENTS_PATH)

    clients = read_json(CLIENTS_PATH)
    for client in clients["clients"]:
        if client["phone"] == phone:
            return False

    employees = read_json(EMPLOYEES_PATH)
    for employee in employees["employees"]:
        if employee["phone"] == phone:
            return False

    return True


# Check if exists nif
def check_nif(nif: str) -> bool:

    check_file(CLIENTS_PATH)

    clients = read_json(CLIENTS_PATH)

    for client in clients["clients"]:
        if client["nif"] == nif:
            return False

    employees = read_json(EMPLOYEES_PATH)

    for employee in employees["employees"]:
        if employee["nif"] == nif:
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


# Validate nif
def validate_nif(nif: str) -> bool:
    if re.match(REGEX_NIF, nif):
        return True

    return False
