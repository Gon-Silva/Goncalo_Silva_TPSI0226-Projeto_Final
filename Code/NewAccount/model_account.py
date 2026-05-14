from GenericUtlis.terminal import press_to_continue
from NewAccount.utils_new_account import (
    check_email,
    validate_age,
    validate_email,
    validate_len_password,
    validate_name,
    validate_phone,
)


class NewAccount:
    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        age: int,
        phone: str,
        email: str,
        password: str,
        is_active: bool,
        subscription_plan: str,
    ) -> None:
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__phone = phone
        self.__email = email
        self.__password = password
        self.__is_active = is_active
        self.__subscription_plan = subscription_plan

    # Getters for private attributes
    @property
    def id(self) -> int:
        """Returns account id"""
        return self.__id

    @property
    def first_name(self) -> str:
        """Returns account first name"""
        return self.__first_name

    @property
    def last_name(self) -> str:
        """Returns account last name"""
        return self.__last_name

    @property
    def age(self) -> int:
        """Returns account age"""
        return self.__age

    @property
    def phone(self) -> str:
        """Returns account phone"""
        return self.__phone

    @property
    def email(self) -> str:
        """Returns account email"""
        return self.__email

    @property
    def password(self) -> str:
        """Returns account password"""
        return self.__password

    @property
    def is_active(self) -> bool:
        """Returns account active"""
        return self.__is_active

    @property
    def subscription_plan(self) -> str:
        """Returns account subscription plan"""
        return self.__subscription_plan

    # Setters for private attributes
    @id.setter
    def id(self, id: int) -> None:
        """Set id"""
        self.__id = id

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        """Set first name"""
        if not validate_name(first_name):
            raise ValueError("Invalid first name size")
            return

        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """Set last name"""
        if not validate_name(last_name):
            raise ValueError("Invalid last name size")
            return

        self.__last_name = last_name

    @age.setter
    def age(self, age: int) -> None:
        """Set age"""
        if not validate_age(age):
            raise ValueError("Invalid age")
            return

        self.__age = age

    @phone.setter
    def phone(self, phone: str) -> None:
        """Set phone"""
        if not validate_phone(phone):
            raise ValueError("Invalid phone format")
            return

        self.__phone = phone

    @email.setter
    def email(self, email: str) -> None:
        """Set email"""
        if not validate_email(email):
            raise ValueError("Invalid email format")
            return

        if not check_email(email):
            raise ValueError("This email address already exists")
            return

        self.__email = email

    @password.setter
    def password(self, password: str) -> None:
        """Set password"""
        if not validate_len_password(password):
            raise ValueError("Invalid passowrd size")
            return

        self.__password = password

    @is_active.setter
    def is_active(self, is_active: bool) -> None:
        """Set is active"""
        self.__is_active = is_active

    @subscription_plan.setter
    def subscription_plan(self, subcription_plan: str) -> None:
        """Set subscription plan"""
        self.__subscription_plan = subcription_plan

    # String representation for debugging/logging
    def __repr__(self) -> str:
        return (
            f"New Account(id -> '{self.__id}'"
            f"first name -> '{self.__first_name}', "
            f"last name -> '{self.__last_name}', "
            f"age -> '{self.__age}', "
            f"phone -> '{self.__phone}', "
            f"email -> '{self.__email}', "
            f"password -> '{self.__password}', "
            f"subscription plan -> '{self.__subscription_plan}', "
            f"is active -> '{self.__is_active}')"
        )

    # String for the user (Need improvement)
    def __str__(self) -> str:
        return (
            f"First Name - {self.__first_name} |"
            f"Last Name  - {self.__last_name} |"
            f"Age        - {self.__age} |"
            f"Phone      - {self.__phone} |"
            f"Email      - {self.__email} |"
            f"Password   - {self.__password} |"
        )

    # Convert the class to dict
    def to_dict(self) -> dict:
        return {
            "id": self.__id,
            "name": {
                "first_name": self.__first_name,
                "last_name": self.__last_name,
            },
            "age": self.__age,
            "phone": self.__phone,
            "email": self.__email,
            "password": self.__password,
            "is_active": self.__is_active,
            "subscription_plan": self.__subscription_plan,
        }
