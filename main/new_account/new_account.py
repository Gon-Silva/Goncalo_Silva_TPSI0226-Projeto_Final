import re

from headers.headers import header_new_account
from new_account.model_account import New_Account
from new_account.utils_new_account import save_account
from utils.errors import catch_number_error
from utils.terminal import cls, press_to_continue


def new_account():

    new_user = New_Account("", 0, "", "", "")
    number = 1

    while True:
        cls()

        print(header_new_account)

        new_user.show_new_account()

        match number:
            case 1:
                # Set name
                name = input("\nSet Name -> ")
                new_user.set_name(name)

                number += 1

            case 2:
                # Set age
                age = catch_number_error("\nSet Age -> ")
                new_user.set_age(age)

                if new_user.get_age() < 16:
                    continue

                number += 1

            case 3:
                # Set phone
                phone = input("\nSet Phone -> ")
                new_user.set_phone(phone)

                if new_user.get_phone() == "":
                    continue

                number += 1

            case 4:
                # Set email
                email = input("\nSet Email -> ")
                new_user.set_email(email)

                if new_user.get_email() == "":
                    continue

                number += 1

            case 5:
                # Set password
                password = input("\nSet Password -> ")
                new_user.set_password(password)

                number += 1

            case _:
                break

    new_user.show_new_account()

    new_user.before_confirming()

    save_account(new_user.to_dict())

    print("Saved successfully")

    press_to_continue()
