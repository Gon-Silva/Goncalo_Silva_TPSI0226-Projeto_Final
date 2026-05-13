# Path
import numbers

from config import STATEMENT_PATH

# My library
from GenericUtlis.errors import catch_number_error
from GenericUtlis.files import create_json, file_exists
from GenericUtlis.terminal import cls, press_to_continue
from Setup.model_setup import Setup
from Setup.setup_utils import (
    validate_date,
    validate_email,
    validate_name,
    validate_phone,
)


def setup():

    # Checks whether the file exists
    if not file_exists(STATEMENT_PATH):
        setup = create_setup()

        while True:
            print(" > Do you want continue in this configuration")
            print(" > [ Y | N ]")
            confirmation = input(" >> ").upper()

            if confirmation == "Y":
                print(" > Preview")
                print(f" > {setup}")
                print(" > Configuration saved")
                create_json(STATEMENT_PATH, setup.to_dict())
                press_to_continue()
                break

            elif confirmation == "N":
                print(" > What do you want to change?")
                print(" [ 1 ] - Name")
                print(" [ 2 ] - Creation Date")
                print(" [ 3 ] - Statement Email")
                print(" [ 4 ] - Statement Phone")
                print(" [ 5 ] - Location")
                print(" [ 0 ] - Exit")

                change_option = catch_number_error(" >> ")

                match change_option:
                    case 1:
                        print(" > Name of Statement")
                        print(" > Ex >> Random Play")
                        setup.name = input(" >> ")
                        pass

                    case 2:
                        print(" > Creation date of Statement")
                        print(" > Ex >> 20-04-2007")
                        setup.creation_date = input(" >> ")
                        pass

                    case 3:
                        print(" > Statement email ")
                        print(" > Ex >> @random.play")
                        setup.statement_email = input(" >> ")
                        pass

                    case 4:
                        print(" > Statement phone ")
                        print(" > Ex >> 936666666")
                        setup.phone = input(" >> ")
                        pass

                    case 5:
                        print(" > Location ")
                        print(" > Street")
                        print(" > Ex >> Rua João das Coves")
                        street = input(" >> ")

                        print(" > City")
                        print(" > Ex >> Lisboa")
                        city = input(" >> ")

                        print(" > Region")
                        print(" > Ex >> Grande Lisboa")
                        region = input(" >> ")

                        print(" > Country")
                        print(" > Ex >> Portugal")
                        country = input(" >> ")

                        setup.location = {
                            "street": street,
                            "city": city,
                            "region": region,
                            "country": country,
                        }

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


def create_setup():

    number = 1

    name = creation_date = statement_email = statement_phone = ""
    street = city = region = country = ""

    while number <= 5:
        cls()

        match number:
            case 1:
                print(" > Name of Statement")
                print(" > Ex >> Random Play")
                name = input(" >> ")

                if not validate_name(name):
                    print("Invalid name size")
                    press_to_continue()
                    continue

                number += 1
            case 2:
                print(" > Creation date of Statement")
                print(" > Ex >> 20-04-2007")
                creation_date = input(" >> ")

                if not validate_date(creation_date):
                    print("Invalid date format")
                    press_to_continue()
                    continue

                number += 1
            case 3:
                print(" > Statement email ")
                print(" > Ex >> @random.play")
                statement_email = input(" >> ")

                if not validate_email(statement_email):
                    print("Invalid email format")
                    press_to_continue()
                    continue

                number += 1

            case 4:
                print(" > Statement phone ")
                print(" > Ex >> 936666666")
                statement_phone = input(" >> ")

                if not validate_phone(statement_phone):
                    print("Invalid phone format")
                    press_to_continue()
                    continue

                number += 1

            case 5:
                print(" > Location Details")
                print(" > Street")
                print(" > Ex >> Rua João das Coves")
                street = input(" >> ")

                print(" > City")
                print(" > Ex >> Lisboa")
                city = input(" >> ")

                print(" > Region")
                print(" > Ex >> Grande Lisboa")
                region = input(" >> ")

                print(" > Country")
                print(" > Ex >> Portugal")
                country = input(" >> ")

                number += 1

    return Setup(
        name,
        creation_date,
        statement_email,
        statement_phone,
        street,
        city,
        region,
        country,
    )
