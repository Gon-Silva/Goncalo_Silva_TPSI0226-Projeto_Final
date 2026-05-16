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
        video_rental_store_email: str,
        video_rental_store_phone: str,
        street: str,
        city: str,
        region: str,
        country: str,
    ) -> None:
        self.__name = name
        self.__creation_date = creation_date
        self.__video_rental_store_email = video_rental_store_email
        self.__video_rental_store_phone = video_rental_store_phone
        self.__street = street
        self.__city = city
        self.__region = region
        self.__country = country

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
    def video_rental_store_email(self) -> str:
        """Returns the owner's email address"""
        return self.__video_rental_store_email

    @property
    def video_rental_store_phone(self) -> str:
        """Returns the phone number"""
        return self.__video_rental_store_phone

    @property
    def street(self) -> str:
        """Returns the street"""
        return self.__street

    @property
    def city(self) -> str:
        """Returns the city"""
        return self.__city

    @property
    def region(self) -> str:
        """Returns the region"""
        return self.__region

    @property
    def country(self) -> str:
        """Returns the country"""
        return self.__country

    @property
    def location(self) -> dict:
        return {
            "street": self.__street,
            "city": self.__city,
            "region": self.__region,
            "country": self.__country,
        }

    # Setters for private attributes
    @name.setter
    def name(self, name: str) -> None:
        """Set the name"""
        if not validate_name(name):
            raise ValueError("\n > Invalid name size")

        self.__name = name

    @creation_date.setter
    def creation_date(self, creation_date: str) -> None:
        """Set the date of creation"""
        if not validate_date(creation_date):
            raise ValueError("\n > Invalid date format")

        self.__creation_date = creation_date

    @video_rental_store_email.setter
    def video_rental_store_email(self, video_rental_store_email: str) -> None:
        """Set the email address"""
        if not validate_email(video_rental_store_email):
            raise ValueError("\n > Invalid email format")

        self.__video_rental_store_email = video_rental_store_email

    @video_rental_store_phone.setter
    def video_rental_store_phone(self, video_rental_store_phone: str) -> None:
        """Set the phone number"""
        if not validate_phone(video_rental_store_phone):
            raise ValueError("\n > Invalid phone format")

        self.__video_rental_store_phone = video_rental_store_phone

    @street.setter
    def street(self, street) -> None:
        """Set the street"""
        self.__street = street

    @city.setter
    def city(self, city) -> None:
        """Set the city"""
        self.__city = city

    @region.setter
    def region(self, region) -> None:
        """Set the region"""
        self.__region = region

    @country.setter
    def country(self, country) -> None:
        """Set the country"""
        self.__country = country

    # String representation for debugging/logging
    def __repr__(self) -> str:
        return (
            f"Setup(name ->'{self.__name}', "
            f"created -> '{self.__creation_date}', "
            f"video_rental_store_email -> '{self.__video_rental_store_email}', "
            f"video_rental_store_phone -> '{self.__video_rental_store_phone}', "
            f"address -> '{self.location}')"
        )

    # String for the user
    def __str__(self) -> str:
        return (
            f" > Video Rental Store Name - {self.__name}\n"
            f" > Create Time - {self.__creation_date}\n"
            f" > Video Rental Store Email - {self.__video_rental_store_email}\n"
            f" > Video Rental Store Phone - {self.__video_rental_store_phone}\n"
            f" > Location\n"
            f"  > Street - {self.__street}\n"
            f"  > City - {self.__city}\n"
            f"  > Region - {self.__region}\n"
            f"  > Country - {self.__country}\n"
        )

    # Convert the class to dict
    def to_dict(self) -> dict:
        return {
            "name": self.__name,
            "creation_date": self.__creation_date,
            "video_rental_store_email": self.__video_rental_store_email,
            "video_rental_store_phone": self.__video_rental_store_phone,
            "location": self.location,
        }
