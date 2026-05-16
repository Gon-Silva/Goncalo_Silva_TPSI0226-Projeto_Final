# Path
from config import STATEMENT_PATH

# My library
from GenericUtlis.errors import catch_number_error
from GenericUtlis.files import create_json, file_exists
from GenericUtlis.terminal import cls, press_to_continue
from Setup.model_setup import Setup


def setup():

    # Checks whether the file exists
    if not file_exists(STATEMENT_PATH):
        setup = create_setup()

        confirm_setup(setup)


def create_setup():

    setup = Setup("", "", "", "", "", "", "", "")

    number = 1

    while number <= 5:
        cls()

        match number:
            case 1:
                print(" > Name of Statement")
                print(" > Ex >> Random Play")
                try:
                    setup.name = input(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1
            case 2:
                print(" > Creation date of Statement")
                print(" > Ex >> 20-04-2007")
                try:
                    setup.creation_date = input(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1
            case 3:
                print(" > Statement email ")
                print(" > Ex >> @random.play")
                try:
                    setup.statement_email = input(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 4:
                print(" > Statement phone ")
                print(" > Ex >> 936666666")
                try:
                    setup.statement_phone = input(" >> ")

                except ValueError as error:
                    print(error)
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

                setup.location = {
                    "street": street,
                    "city": city,
                    "region": region,
                    "country": country,
                }

                number += 1

    return setup


def confirm_setup(setup: Setup):
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
                    try:
                        setup.name = input(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()
                        continue

                case 2:
                    print(" > Creation date of Statement")
                    print(" > Ex >> 20-04-2007")
                    try:
                        setup.creation_date = input(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()
                        continue

                case 3:
                    print(" > Statement email ")
                    print(" > Ex >> @random.play")
                    try:
                        setup.statement_email = input(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()
                        continue

                case 4:
                    print(" > Statement phone ")
                    print(" > Ex >> 936666666")
                    try:
                        setup.statement_phone = input(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()
                        continue

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
