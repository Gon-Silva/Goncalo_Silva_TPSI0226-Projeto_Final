# My library
from Setup.setup_utils import (
    validate_date,
    validate_email,
    validate_name,
    validate_phone,
)


class Setup:
    def __init__(
        self,
        name: str,
        creation_date: str,
        statement_email: str,
        statement_phone: str,
        street: str,
        city: str,
        region: str,
        country: str,
    ) -> None:
        self.__name = name
        self.__creation_date = creation_date
        self.__statement_email = statement_email
        self.__statement_phone = statement_phone
        self.__location = {
            "street": street,
            "city": city,
            "region": region,
            "country": country,
        }

    # Getters for private attributes
    @property
    def name(self) -> str:
        """Returns the setup name"""
        return self.__name

    @property
    def creation_date(self) -> str:
        """Returns the creation date"""
        return self.__creation_date

    @property
    def statement_email(self) -> str:
        """Returns the owner's email address"""
        return self.__statement_email

    @property
    def statement_phone(self) -> str:
        """Returns the phone number"""
        return self.__statement_phone

    @property
    def location(self) -> str:
        """Returns the full address as a formatted string"""
        loc = self.__location
        return f"{loc['street']}, {loc['city']}, {loc['region']}, {loc['country']}"

    # Setters for private attributes
    @name.setter
    def name(self, name: str) -> None:
        """Set the name"""
        if not validate_name(name):
            raise ValueError("Invalid name size")

        self.__name = name

    @creation_date.setter
    def creation_date(self, creation_date: str) -> None:
        """Set the date of creation"""
        if not validate_date(creation_date):
            raise ValueError("Invalid date format")

        self.__creation_date = creation_date

    @statement_email.setter
    def statement_email(self, statement_email: str) -> None:
        """Set the email address"""
        if not validate_email(statement_email):
            raise ValueError("Invalid email format")

        self.__statement_email = statement_email

    @statement_phone.setter
    def statement_phone(self, statement_phone: str) -> None:
        """Set the phone number"""
        if not validate_phone(statement_phone):
            raise ValueError("Invalid phone format")

        self.__statement_phone = statement_phone

    @location.setter
    def location(self, location: dict) -> None:
        """Set the location"""
        self.__location = location

    # String representation for debugging/logging
    def __repr__(self) -> str:
        return (
            f"Setup(name ->'{self.__name}', "
            f"created -> '{self.__creation_date}', "
            f"statement_email -> '{self.__statement_email}', "
            f"address -> '{self.location}')"
        )

    # String for the user
    def __str__(self) -> str:
        return f"{self.__name} | {self.location}"

    # Convert the class to dict
    def to_dict(self) -> dict:
        return {
            "name": self.__name,
            "creation_date": self.__creation_date,
            "owners_email": self.__statement_email,
            "location": self.__location,
        }
