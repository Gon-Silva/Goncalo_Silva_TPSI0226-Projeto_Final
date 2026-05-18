# Path
from config import CLIENTS_PATH, EMPLOYEES_PATH

# My library
from GenericUtlis.errors import catch_number_error
from GenericUtlis.files import read_json
from GenericUtlis.input import (
    input_age,
    input_email_client,
    input_name,
    input_nif,
    input_password,
    input_phone,
)
from GenericUtlis.terminal import cls, press_to_continue
from Headers.headers import header_confirm, header_new_account
from NewAccount.model_account import NewClient, NewEmployee
from NewAccount.utils_new_account import check_file, save_account


def new_account_client():

    new_account = create_account_client()

    confirm_new_account_client(new_account)


def new_account_employee():

    new_account = create_account_employee()

    confirm_new_account_employee(new_account)


def create_account_client():

    check_file(CLIENTS_PATH)

    clients_db = read_json(CLIENTS_PATH)

    if clients_db is None:
        clients_db = {"next_id": 1, "clients": []}

    new_id = clients_db["next_id"]

    new_account = NewClient(new_id, "", "", 0, "", "", "", "", True, "basic")

    number = 1

    while number <= 7:
        cls()

        print(header_new_account)

        match number:
            case 1:
                print("\n > First Name")
                print(" > Ex >> Ana")
                try:
                    new_account.first_name = input_name(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 2:
                print("\n > Last Name")
                print(" > Ex >> Silva")
                try:
                    new_account.last_name = input_name(" >> ")
                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 3:
                print("\n > Age")
                print(" > Ex >> 18")
                try:
                    new_account.age = input_age(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 4:
                print("\n > Phone")
                print(" > Ex >> 932751849")
                try:
                    new_account.phone = input_phone(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 5:
                print("\n > Do you want to enter your tax ID number?")
                print(" > [ Y | N ]")
                confirmation = input(" >> ").upper()

                if confirmation == "Y":
                    print("\n > NIF")
                    print(" > Ex >> 267887954")
                    try:
                        new_account.nif = input_nif(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()
                        continue

                    number += 1

                elif confirmation == "N":
                    new_account.nif = None
                    number += 1

                else:
                    print("\n > [ ERROR ]")
                    print(" > Enter a validate option")
                    press_to_continue()

            case 6:
                print("\n > Email ")
                print(" > Ex >> ana.silva@gmail.com")
                try:
                    new_account.email = input_email_client(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 7:
                print("\n > Password ")
                print(" > Ex >> Dia-45-89&&&asdasd")
                try:
                    new_account.password = input_password(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

    return new_account


def create_account_employee():

    check_file(EMPLOYEES_PATH)

    employee_db = read_json(EMPLOYEES_PATH)

    if employee_db is None:
        employee_db = {"next_id": 1, "employees": []}

    new_id = employee_db["next_id"]

    new_account = NewEmployee(new_id, "", "", 0, "", "", "", "", True, "")

    number = 1

    while number <= 6:
        cls()

        match number:
            case 1:
                print("\n > First Name")
                print(" > Ex >> Ana")
                try:
                    new_account.first_name = input_name(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 2:
                print("\n > Last Name")
                print(" > Ex >> Silva")
                try:
                    new_account.last_name = input_name(" >> ")
                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 3:
                print("\n > Age")
                print(" > Ex >> 18")
                try:
                    new_account.age = input_age(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 4:
                print("\n > Phone")
                print(" > Ex >> 932751849")
                try:
                    new_account.phone = input_phone(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 5:
                print("\n > NIF")
                print(" > Ex >> 267887954")
                try:
                    new_account.nif = input_nif(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 6:
                print("\n > Role")
                print(" > Select a role")
                print(" [ 1 ] - Owner")
                print(" [ 2 ] - Employee")

                try:
                    select_role = catch_number_error("\n >>")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                match select_role:
                    case 1:
                        new_account.role = "owner"
                        pass

                    case 2:
                        new_account.role = "employee"
                        pass

                    case _:
                        print("\n > [ ERROR ]")
                        print(" > Enter a validate option")
                        press_to_continue()
                        pass

                number += 1

    return new_account


def confirm_new_account_client(new_account: NewClient):
    while True:
        cls()

        print(header_confirm)

        print(new_account)

        print("\n > Do you want continue in this configuration")
        print(" > [ Y | N ]")
        confirmation = input(" >> ").upper()

        if confirmation == "Y":
            print("\n > Preview\n")
            print(new_account)
            print("\n > Configuration saved")
            save_account(new_account.to_dict(), CLIENTS_PATH)
            press_to_continue()
            break

        elif confirmation == "N":
            cls()

            print(" > What do you want to change?")
            print(" [ 1 ] - Fisrt Name")
            print(" [ 2 ] - Last Name")
            print(" [ 3 ] - Age")
            print(" [ 4 ] - Phone")
            print(" [ 5 ] - NIF")
            print(" [ 6 ] - Email")
            print(" [ 7 ] - Password")
            print(" [ 0 ] - Exit ")

            try:
                change_option = catch_number_error("\n >> ")

            except ValueError as error:
                print(error)
                press_to_continue()
                continue

            match change_option:
                case 1:
                    print("\n > First Name")
                    print(" > Ex >> Ana")
                    try:
                        new_account.first_name = input_name(" >> ")
                    except ValueError as error:
                        print(error)
                        press_to_continue()

                case 2:
                    print("\n > Last Name")
                    print(" > Ex >> Silva")
                    try:
                        new_account.last_name = input_name(" >> ")
                    except ValueError as error:
                        print(error)
                        press_to_continue()

                case 3:
                    print("\n > Age")
                    print(" > Ex >> 18")
                    try:
                        new_account.age = input_age(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()

                case 4:
                    print("\n > Phone")
                    print(" > Ex >> 932751849")
                    try:
                        new_account.phone = input_phone(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()

                case 5:
                    print("\n > NIF")
                    print(" > Ex >> 267887954")
                    try:
                        new_account.nif = input_nif(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()

                case 6:
                    print("\n > Email ")
                    print(" > Ex >> ana.silva@gmail.com")
                    try:
                        new_account.email = input_email_client(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()

                case 7:
                    print("\n > Password ")
                    print(" > Ex >> Dia-45-89&&&asdasd")
                    try:
                        new_account.password = input_password(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()

                case 0:
                    print("\n > Back to confirmation")
                    press_to_continue()
                    pass

                case _:
                    print("\n > [ ERROR ]")
                    print(" > Enter a validate option")
                    press_to_continue()
                    pass

        else:
            print("\n > [ ERROR ]")
            print(" > Enter a validate option")
            press_to_continue()


def confirm_new_account_employee(new_account: NewEmployee):
    while True:
        cls()

        print(header_confirm)

        print(new_account)

        print("\n > Do you want continue in this configuration")
        print(" > [ Y | N ]")
        confirmation = input(" >> ").upper()

        if confirmation == "Y":
            print("\n > Preview\n")
            print(new_account)
            print("\n > Configuration saved")
            save_account(new_account.to_dict(), EMPLOYEES_PATH)
            press_to_continue()
            break

        elif confirmation == "N":
            cls()

            print(" > What do you want to change?")
            print(" [ 1 ] - Fisrt Name")
            print(" [ 2 ] - Last Name")
            print(" [ 3 ] - Age")
            print(" [ 4 ] - Phone")
            print(" [ 5 ] - NIF")
            print(" [ 6 ] - Role")
            print(" [ 0 ] - Exit ")

            try:
                change_option = catch_number_error("\n >> ")

            except ValueError as error:
                print(error)
                press_to_continue()
                continue

            match change_option:
                case 1:
                    print("\n > First Name")
                    print(" > Ex >> Ana")
                    try:
                        new_account.first_name = input_name(" >> ")
                    except ValueError as error:
                        print(error)
                        press_to_continue()

                case 2:
                    print("\n > Last Name")
                    print(" > Ex >> Silva")
                    try:
                        new_account.last_name = input_name(" >> ")
                    except ValueError as error:
                        print(error)
                        press_to_continue()

                case 3:
                    print("\n > Age")
                    print(" > Ex >> 18")
                    try:
                        new_account.age = input_age(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()

                case 4:
                    print("\n > Phone")
                    print(" > Ex >> 932751849")
                    try:
                        new_account.phone = input_phone(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()

                case 5:
                    print("\n > NIF")
                    print(" > Ex >> 267887954")
                    try:
                        new_account.nif = input_nif(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()

                case 6:
                    print("\n > Role")
                    print(" > Select a role")
                    print(" [ 1 ] - Owner")
                    print(" [ 2 ] - Employee")
                    print(" [ 0 ] - Employee")

                    try:
                        select_role = catch_number_error("\n >>")

                    except ValueError as error:
                        print(error)
                        press_to_continue()
                        continue

                    match select_role:
                        case 1:
                            new_account.role = "owner"
                            pass

                        case 2:
                            new_account.role = "employee"
                            pass

                        case 0:
                            print("\n > Back to confirmation")
                            press_to_continue()
                            break

                        case _:
                            print("\n > [ ERROR ]")
                            print(" > Enter a validate option")
                            press_to_continue()
                            pass

                case 0:
                    print("\n > Back to confirmation")
                    press_to_continue()
                    pass

                case _:
                    print("\n > [ ERROR ]")
                    print(" > Enter a validate option")
                    press_to_continue()
                    pass

        else:
            print("\n > [ ERROR ]")
            print(" > Enter a validate option")
            press_to_continue()
