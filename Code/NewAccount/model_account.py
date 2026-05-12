import re

from GenericUtlis.errors import catch_number_error
from GenericUtlis.files import read_json
from GenericUtlis.terminal import cls, press_to_continue
from Headers.headers import header_change, header_confirm
from NewAccount.utils_new_account import check_email


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

    def set_age(self, age: int) -> None:
        if age < 16:
            print("Age cannot be negative or under 16 years")
            press_to_continue()
            return

        self.__age = age

    def set_phone(self, phone: str) -> None:

        regex_phone = "^\\+?[1-9][0-9]{7,14}$"

        if not re.match(regex_phone, phone):
            print("Invalid phone format")
            press_to_continue()
            return

        self.__phone = phone

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

    def set_password(self, password: str) -> None:
        self.__password = password

    # Method
    def before_confirming(self) -> None:

        while True:
            cls()

            print(header_confirm)

            self.show_new_account()

            want_change = input(
                "\nDo you want to change something [y or n] -> "
            ).lower()

            if not want_change == "y" and not want_change == "n":
                print("\nPlease select y or n")
                press_to_continue()
                continue

            if want_change == "n":
                return

            if want_change == "y":
                while True:
                    cls()

                    print(header_change)

                    print("[1] - Name")
                    print("[2] - Age")
                    print("[3] - Phone")
                    print("[4] - Email")
                    print("[5] - Password")
                    print("[0] - Back")

                    number_to_change = catch_number_error(
                        "\nSelect an option do you want change -> "
                    )

                    if number_to_change is None:
                        continue

                    match number_to_change:
                        case 0:
                            break
                        case 1:
                            name = input("\nSet Name - > ")
                            self.set_name(name)
                            break
                        case 2:
                            age = catch_number_error("\nSet Age -> ")
                            self.set_age(age)
                            break
                        case 3:
                            phone = input("\nSet Phone -> ")
                            self.set_phone(phone)
                            break
                        case 4:
                            email = input("\nSet Email -> ")
                            self.set_email(email)
                            break
                        case 5:
                            password = input("\nSet Password -> ")
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

    def show_new_account(self) -> None:

        print(f"Name     - {self.get_name()}")
        print(f"Age      - {self.get_age()}")
        print(f"Phone    - {self.get_phone()}")
        print(f"Email    - {self.get_email()}")
        print(f"Password - {self.get_password()}")
