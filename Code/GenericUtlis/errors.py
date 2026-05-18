# Python library
import re

# Path
from config import (
    CLIENTS_PATH,
    EMPLOYEES_PATH,
    REGEX_EMAIL,
    REGEX_NIF,
    REGEX_PHONE,
    VIDEO_RENTAL_STORE_PATH,
)

# My Library
from GenericUtlis.files import (
    check_file,
    read_json,
)


def catch_number_error(message: str):
    try:
        return int(input(message))
    except ValueError:
        raise ValueError("\n[ERROR] The input must be a number")


# Check if exists email in client db
def check_email_client(email: str) -> bool:

    check_file(CLIENTS_PATH)

    clients = read_json(CLIENTS_PATH)

    for client in clients["clients"]:
        if client["email"] == email:
            return False

    return True


# Check if exists email in client db
def check_email_employee(email: str) -> bool:

    check_file(EMPLOYEES_PATH)

    employees = read_json(EMPLOYEES_PATH)

    for employee in employees["clients"]:
        if employee["email"] == email:
            return False

    return True


# Checks if the email address belongs to the store's domain
def check_domain_store(email: str) -> bool:

    video_rental_store = read_json(VIDEO_RENTAL_STORE_PATH)

    domain = video_rental_store["video_rental_store_email"]
    if email.endswith(domain):
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
