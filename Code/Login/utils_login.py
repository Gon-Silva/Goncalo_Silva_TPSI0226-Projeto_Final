from config import CLIENTS_PATH, EMPLOYEES_PATH, VIDEO_RENTAL_STORE_PATH
from GenericUtlis.files import read_json


# Verify the user
def verify_user(email: str):

    if is_employee(email):
        db = read_json(EMPLOYEES_PATH)
        for data in db["employees"]:
            if data["email"] == email:
                return data

    else:
        db = read_json(CLIENTS_PATH)
        for data in db["clients"]:
            if data["email"] == email:
                return data

    return None


# Verify the password
def verify_password(client: dict, password: str):

    if client["password"] == password:
        return True

    return False


# Check if the email belong to employee
def is_employee(email: str) -> bool:

    vidoe_rental_store = read_json(VIDEO_RENTAL_STORE_PATH)

    domain = vidoe_rental_store["video_rental_store_email"]

    return email.endswith(domain)
