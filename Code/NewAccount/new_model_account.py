from GenericUtlis.terminal import press_to_continue
from NewAccount.utils_new_account import (
    check_email,
    save_account,
    validate_email,
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
        is_active: bool,
        email: str,
        subscription_plan: str,
        password: str,
    ) -> None:
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__phone = phone
        self.__is_active = is_active
        self.__email = email
        self.__subscription_plan = subscription_plan
        self.__password = password

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
    def is_active(self) -> bool:
        """Returns account active"""
        return self.__is_active

    @property
    def email(self) -> str:
        """Returns account email"""
        return self.__email

    @property
    def subscription_plan(self) -> str:
        """Returns account subscription plan"""
        return self.__subscription_plan

    @property
    def password(self) -> str:
        """Returns account password"""
        return self.__password

    # Setters for private attributes
    @id.setter
    def id(self, id: int) -> None:
        """Set id"""
        self.__id = id

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        """Set first name"""
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """Set last name"""
        self.__last_name = last_name

    @age.setter
    def age(self, age: int) -> None:
        """Set age"""
        self.__age = age

    @phone.setter
    def phone(self, age: str) -> None:
        """Set phone"""
        self.__phone = age

    @is_active.setter
    def is_active(self, is_active: bool) -> None:
        """Set is active"""
        self.__is_active = is_active

    @email.setter
    def email(self, email: str) -> None:
        """Set email"""
        self.__email = email

    @subscription_plan.setter
    def subscription_plan(self, subcription_plan: str) -> None:
        """Set subscription plan"""
        self.__subscription_plan = subcription_plan

    @password.setter
    def password(self, password: str) -> None:
        """Set password"""
        self.__password = password
