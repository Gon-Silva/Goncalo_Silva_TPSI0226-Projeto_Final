# Python library
import re
from datetime import datetime

# Regex code
from config import REGEX_EMAIL, REGEX_PHONE


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


# Validate the creation date format
def validate_date(date: str):
    try:
        datetime.strptime(date, "%d-%m-%Y")
        return True
    except ValueError:
        return False


# Validate the size of name
def validate_name(name: str):
    if len(name) == 0:
        return False

    return True
