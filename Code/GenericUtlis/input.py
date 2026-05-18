from GenericUtlis.errors import (
    catch_number_error,
    check_domain_store,
    check_email_client,
    check_email_employee,
    check_nif,
    check_phone,
    validate_age,
    validate_email,
    validate_len_password,
    validate_name,
    validate_nif,
    validate_phone,
)


def input_name(message: str) -> str:
    value = input(message)
    if not validate_name(value):
        raise ValueError("\n > [ERROR] Invalid size")

    return value


def input_age(message: str) -> int:
    value = catch_number_error(message)
    if not validate_age(value):
        raise ValueError("\n > [ERROR] Invalid age")

    return value


def input_phone(message: str) -> str:
    value = input(message)
    if not validate_phone(value):
        raise ValueError("\n > [ERROR] Invalid phone format")

    if not check_phone(value):
        raise ValueError("\n > [ERROR] This phone already exists")

    return value


def input_nif(message: str) -> str:
    value = input(message)
    if not validate_nif(value):
        raise ValueError("\n > [ERROR] Invalid NIF formant")

    if not check_nif(value):
        raise ValueError("\n > [ERROR] This nif already exists")

    return value


def input_email_client(message: str) -> str:
    value = input(message)
    if not validate_email(value):
        raise ValueError("\n > [ERROR] Invalid email format")

    if not check_domain_store(value):
        raise ValueError("\n > [ERROR] Sorry but you can't use this domain")

    if not check_email_client(value):
        raise ValueError("\n > [ERROR] This email address already exists")

    return value


def input_email_employee(message: str) -> str:
    value = input(message)
    if not validate_email(value):
        raise ValueError("\n > [ERROR] Invalid email format")

    if not check_email_employee(value):
        raise ValueError("\n > [ERROR] This email address already exists")

    return value


def input_password(message: str) -> str:
    value = input(message)
    if not validate_len_password(value):
        raise ValueError("\n > [ERROR] Invalid passowrd size")

    return value
