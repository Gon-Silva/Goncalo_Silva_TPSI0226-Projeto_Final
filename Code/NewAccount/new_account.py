# Path
from config import CLIENTS_PATH

# My library
from GenericUtlis.errors import catch_number_error
from GenericUtlis.files import read_json
from GenericUtlis.terminal import cls, press_to_continue
from Headers.headers import header_new_account
from NewAccount.model_account import NewAccount
from NewAccount.utils_new_account import save_account


def new_account():

    create_account()


def create_account():

    clients_db = read_json(CLIENTS_PATH)

    if clients_db is None:
        clients_db = {}

    new_account = NewAccount(len(clients_db) + 1, "", "", 0, "", "", "", True, "basic")

    number = 1

    while number <= 6:
        cls()

        print(header_new_account)

        match number:
            case 1:
                print(" > First Name")
                print(" > Ex >> Ana")
                try:
                    new_account.first_name = input(" >> ")

                except ValueError as error:
                    print(error)
                    continue

                number += 1

            case 2:
                print(" > Last Name")
                print(" > Ex >> Silva")
                try:
                    new_account.last_name = input(" >> ")
                except ValueError as error:
                    print(error)
                    continue

                number += 1

            case 3:
                print(" > Age")
                print(" > Ex >> 18")
                try:
                    new_account.age = catch_number_error(" >> ")

                except ValueError as error:
                    print(error)
                    continue

                number += 1

            case 4:
                print(" > Phone")
                print(" > Ex >> 932751849")
                try:
                    new_account.phone = input(" >> ")

                except ValueError as error:
                    print(error)
                    continue

                number += 1

            case 5:
                print(" > Email ")
                print(" > Ex >> ana.silva@gmail.com")
                try:
                    new_account.email = input(" >> ")

                except ValueError as error:
                    print(error)
                    continue

                number += 1

            case 6:
                print(" > Password ")
                print(" > Ex >> Dia-45-89&&&asdasd")
                try:
                    new_account.password = input(" >> ")

                except ValueError as error:
                    print(error)
                    continue

                number += 1

    return new_account


def confirm_new_account(new_account: NewAccount):
    while True:
        print(" > Do you want continue in this configuration")
        print(" > [ Y | N ]")
        confirmation = input(" >> ").upper()

        if confirmation == "Y":
            print(" > Preview")
            print(f" > {new_account}")
            print(" > Configuration saved")
            save_account(new_account.to_dict())
            press_to_continue()
            break

        elif confirmation == "N":
            print(" > What do you want to change?")
            print(" [ 1 ] - Fisrt Name")
            print(" [ 2 ] - Last Name")
            print(" [ 3 ] - Age")
            print(" [ 4 ] - Phone")
            print(" [ 5 ] - Email")
            print(" [ 6 ] - Password")
            print(" [ 0 ] - Exit ")

            change_option = catch_number_error(" >> ")

            match change_option:
                case 1:
                    print(" > First Name")
                    print(" > Ex >> Ana")
                    try:
                        new_account.first_name = input(" >> ")
                    except ValueError as error:
                        print(error)

                case 2:
                    print(" > Last Name")
                    print(" > Ex >> Silva")
                    try:
                        new_account.last_name = input(" >> ")
                    except ValueError as error:
                        print(error)

                case 3:
                    print(" > Age")
                    print(" > Ex >> 18")
                    try:
                        new_account.age = catch_number_error(" >> ")

                    except ValueError as error:
                        print(error)

                case 4:
                    print(" > Phone")
                    print(" > Ex >> 932751849")
                    try:
                        new_account.phone = input(" >> ")

                    except ValueError as error:
                        print(error)

                case 5:
                    print(" > Email ")
                    print(" > Ex >> ana.silva@gmail.com")
                    try:
                        new_account.email = input(" >> ")

                    except ValueError as error:
                        print(error)

                case 6:
                    print(" > Password ")
                    print(" > Ex >> Dia-45-89&&&asdasd")
                    try:
                        new_account.password = input(" >> ")

                    except ValueError as error:
                        print(error)

                case 0:
                    print(" > Back to confirmation")
                    press_to_continue()
                    pass
                case _:
                    print(" > [ ERROR ]")
                    print(" > Enter a validate option")
                    press_to_continue()
                    pass

        else:
            print(" > [ ERROR ]")
            print(" > Enter a validate option")
            press_to_continue()
