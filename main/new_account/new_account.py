import re

from headers.headers import header_new_account
from new_account.utils_new_account import check_email, save_account
from utils.errors import catch_number_error
from utils.files import read_json
from utils.terminal import cls, press_to_continue


class New_Account:
    def __init__(self, name: str, age: int, phone: str, email: str, password: str):

        # Constructor to initialize the account with private attributes
        self.__name = name
        self.__age = age
        self.__phone = phone
        self.__email = email
        self.__password = password

    # Getters (Accessors)
    def get_name(self) -> str:
        return self.__name

    def get_age(self) -> int:
        return self.__age

    def get_phone(self) -> str:
        return self.__phone

    def get_email(self) -> str:
        return self.__email

    def get_password(self) -> str:
        return self.__password

    # Setters (Mutators)
    def set_name(self, name: str) -> None:
        self.__name = name

        print("Success")
        press_to_continue()

    def set_age(self, age: int) -> None:
        if age < 16:
            print("Age cannot be negative or under 16 years")
            press_to_continue()
        else:
            print("Success")
            press_to_continue()
            self.__age = age

    def set_phone(self, phone: str) -> None:

        regex_phone = "^\\+?[1-9][0-9]{7,14}$"

        if not re.match(regex_phone, phone):
            print("Invalid phone format")
            return

        print("Success")
        self.__phone = phone

        press_to_continue()

    def set_email(self, email: str) -> None:

        data_clients = read_json("data_base/clients/clients.json")

        regex_email = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not re.match(regex_email, email):
            print("Invalid email format")
            press_to_continue()
            return

        if not check_email(data_clients, email):
            print("This email address is already in use")
            press_to_continue()
            return

        self.__email = email
        print("Success")

        press_to_continue()

    def set_password(self, password: str) -> None:
        self.__password = password

    # Method
    def before_confirming(self) -> None:

        while True:
            cls()

            print("Do you want to change something?")

            want_change = input("[y or n] -> ").lower()

            if not want_change == "y" and not want_change == "n":
                print("Please select y or n")

                press_to_continue()
                continue

            if want_change == "n":
                return

            if want_change == "y":
                while True:
                    cls()

                    print("[1] - Name")
                    print("[2] - Age")
                    print("[3] - Phone")
                    print("[4] - Email")
                    print("[5] - Password")
                    print("[0] - Back")

                    number_to_change = catch_number_error(
                        "Select an option do you want change -> "
                    )

                    if number_to_change is None:
                        continue

                    match number_to_change:
                        case 0:
                            break
                        case 1:
                            name = input("Name - ")
                            self.set_name(name)
                            break
                        case 2:
                            age = catch_number_error("Age - ")
                            self.set_age(age)
                            break
                        case 3:
                            phone = input("Phone - ")
                            self.set_phone(phone)
                            break
                        case 4:
                            email = input("Email - ")
                            self.set_email(email)
                            break
                        case 5:
                            password = input("Password - ")
                            self.set_password(password)
                            break
                        case _:
                            print("\n[ERROR] Between 1 and 5")
                            press_to_continue()

    def to_dict(self) -> dict:
        return {
            "name": self.__name,
            "age": self.__age,
            "phone": self.__phone,
            "email": self.__email,
            "password": self.__password,
        }

    def confirm(self) -> str:

        # Returns a confirmation string summarizing the account details

        return (
            f"\nAccount Confirmed!\n\n"
            f"Name: {self.__name}\n"
            f"Age: {self.__age}\n"
            f"Phone: {self.__phone}\n"
            f"Email: {self.__email}\n"
            f"Password: {self.__password}"
        )

    def show_new_account(self) -> None:

        print(f"Name     - {self.get_name()}")
        print(f"Age      - {self.get_age()}")
        print(f"Phone    - {self.get_phone()}")
        print(f"Email    - {self.get_email()}")
        print(f"Password - {self.get_password()}")


def new_account():

    new_user = New_Account("", 0, "", "", "")
    number = 1

    while True:
        cls()

        new_user.show_new_account()

        match number:
            case 1:
                # Set name
                print("\nSet Name")
                name = input("\n > ")
                new_user.set_name(name)

                number += 1

            case 2:
                # Set age
                print("\nSet Age")
                age = catch_number_error("\n > ")
                new_user.set_age(age)

                if new_user.get_age() < 16:
                    continue

                number += 1

            case 3:
                # Set phone
                print("\nSet Phone")
                phone = input("\n > ")
                new_user.set_phone(phone)

                if new_user.get_phone() == "":
                    continue

                number += 1

            case 4:
                # Set email
                print("\nSet Email")
                email = input("\n > ")
                new_user.set_email(email)

                if new_user.get_email() == "":
                    continue

                number += 1

            case 5:
                # Set password
                print("\nSet Password")
                password = input("\n > ")
                new_user.set_password(password)

                number += 1

            case _:
                break

    new_user.show_new_account()

    new_user.before_confirming()

    print(new_user.confirm())

    save_account(new_user.to_dict())

    press_to_continue()
