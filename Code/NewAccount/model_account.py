from config import VIDEO_RENTAL_STORE_PATH
from GenericUtlis.files import read_json
from NewAccount.utils_new_account import (
    check_email,
    check_nif,
    check_phone,
    validate_age,
    validate_email,
    validate_len_password,
    validate_name,
    validate_nif,
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
        nif: str,
        email: str,
        password: str,
        is_active: bool,
    ) -> None:
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__phone = phone
        self.__nif = nif
        self.__email = email
        self.__password = password
        self.__is_active = is_active

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
    def nif(self) -> str:
        """Returns NIF account"""
        return self.__nif

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

        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """Set last name"""
        if not validate_name(last_name):
            raise ValueError("Invalid last name size")

        self.__last_name = last_name

    @age.setter
    def age(self, age: int) -> None:
        """Set age"""
        if not validate_age(age):
            raise ValueError("Invalid age")

        self.__age = age

    @phone.setter
    def phone(self, phone: str) -> None:
        """Set phone"""
        if not validate_phone(phone):
            raise ValueError("Invalid phone format")

        if not check_phone(phone):
            raise ValueError("This phone already exists")

        self.__phone = phone

    @nif.setter
    def nif(self, nif: str) -> None:
        """Set NIF"""
        if not validate_nif(nif):
            raise ValueError("Invalid NIF formant")

        if not check_nif(nif):
            raise ValueError("This nif already exists")

        self.__nif = nif

    @email.setter
    def email(self, email: str) -> None:
        """Set email"""
        if not validate_email(email):
            raise ValueError("Invalid email format")

        if not check_email(email):
            raise ValueError("This email address already exists")

        self.__email = email

    @password.setter
    def password(self, password: str) -> None:
        """Set password"""
        if not validate_len_password(password):
            raise ValueError("Invalid passowrd size")

        self.__password = password

    @is_active.setter
    def is_active(self, is_active: bool) -> None:
        """Set is active"""
        self.__is_active = is_active

    # String representation for debugging/logging
    def __repr__(self) -> str:
        return (
            f"New Account(id -> '{self.__id}'"
            f"first name -> '{self.__first_name}', "
            f"last name -> '{self.__last_name}', "
            f"age -> '{self.__age}', "
            f"phone -> '{self.__phone}', "
            f"nif -> '{self.__nif}', "
            f"email -> '{self.__email}', "
            f"password -> '{self.__password}', "
            f"is active -> '{self.__is_active}'), "
        )

    # String for the user (Need improvement)
    def __str__(self) -> str:
        return (
            f" > First Name - {self.__first_name}\n"
            f" > Last Name - {self.__last_name}\n"
            f" > Age - {self.__age}\n"
            f" > Phone - {self.__phone}\n"
            f" > NIF - {self.__nif}\n"
            f" > Email - {self.__email}\n"
            f" > Password - {self.__password}"
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
            "nif": self.__nif,
            "email": self.__email,
            "password": self.__password,
            "is_active": self.__is_active,
        }


class NewClient(NewAccount):
    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        age: int,
        phone: str,
        nif: str,
        email: str,
        password: str,
        is_active: bool,
        subscription_plan: str,
    ) -> None:
        super().__init__(
            id,
            first_name,
            last_name,
            age,
            phone,
            nif,
            email,
            password,
            is_active,
        )
        self.__subscription_plan = subscription_plan

    # Getters for private attributes
    @property
    def subscription_plan(self) -> str:
        """Returns account subscription plan"""
        return self.__subscription_plan

    # Setters for private attributes
    @subscription_plan.setter
    def subscription_plan(self, subcription_plan: str) -> None:
        """Set subscription plan"""
        self.__subscription_plan = subcription_plan

    # String representation for debugging/logging
    def __repr__(self) -> str:
        return f"{super().__repr__()}\n > Subscription Plan -> '{self.__subscription_plan}'"

    # String for the user (Need improvement)
    def __str__(self) -> str:
        return super().__str__()

    # Convert the class to dict
    def to_dict(self) -> dict:
        base = super().to_dict()
        base["subscription_plan"] = self.__subscription_plan
        return base


class NewEmployee(NewAccount):
    def __init__(
        self,
        id: int,
        first_name: str,
        last_name: str,
        age: int,
        phone: str,
        nif: str,
        email: str,
        password: str,
        is_active: bool,
        role: str,
    ) -> None:
        super().__init__(
            id, first_name, last_name, age, phone, nif, email, password, is_active
        )
        self.__role = role

    # Getters for private attributes

    @property
    def role(self) -> str:
        """Returns role account"""
        return self.__role

    # Setters for private attributes
    @role.setter
    def role(self, role: str) -> None:
        """Set role"""
        self.__role = role

    # String representation for debugging/logging
    def __repr__(self) -> str:
        self.update_email()
        self.create_temp_password()
        return f"{super().__repr__()}\nrole -> '{self.__role}' ,"

    # String for the user (Need improvement)
    def __str__(self) -> str:
        self.update_email()
        self.create_temp_password()
        return f"{super().__str__()}\n > Role -> '{self.__role}'"

    # Update email with
    def update_email(self) -> None:
        video_rental_store = read_json(VIDEO_RENTAL_STORE_PATH)
        self.email = f"{self.first_name.lower()}.{self.last_name.lower()}{video_rental_store['video_rental_store_email']}"

    # create a temp password
    def create_temp_password(self) -> None:
        self.password = "temp-pass"

    # Convert the class to dict
    def to_dict(self) -> dict:
        self.update_email()
        self.create_temp_password()
        base = super().to_dict()
        base["role"] = self.__role
        return base
