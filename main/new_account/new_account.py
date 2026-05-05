from headers.headers import header_new_account
from new_account.utils_new_account import save_account
from utils.errors import catch_number_error
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

    def set_age(self, age: int) -> None:
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self.__age = age

    def set_phone(self, phone: str) -> None:
        self.__phone = phone

    def set_email(self, email: str) -> None:
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        self.__email = email

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


def new_account():
    cls()

    print(header_new_account)

    name = input("Name - ")
    age = catch_number_error("Age - ")
    phone = input("Phone - ")
    email = input("Email - ")
    password = input("Password - ")

    user = New_Account(name, age, phone, email, password)

    user.before_confirming()

    print(user.confirm())

    save_account(user.to_dict())

    press_to_continue()
