# Path
from config import EMPLOYEES_PATH, VIDEO_RENTAL_STORE_PATH

# My library
from GenericUtlis.errors import catch_number_error
from GenericUtlis.files import create_json, file_exists
from GenericUtlis.terminal import cls, press_to_continue
from Headers.headers import header_confirm
from Setup.model_setup import Setup

from Code.NewAccount.model_account import NewEmployee


def setup():

    # Checks whether the file exists
    if not file_exists(VIDEO_RENTAL_STORE_PATH):
        setup = create_setup()

        confirm_setup(setup)

    if not file_exists(EMPLOYEES_PATH):
        new_employee = NewEmployee


def create_setup():

    setup = Setup("", "", "", "", "", "", "", "")

    number = 1

    while number <= 8:
        cls()

        match number:
            case 1:
                print(" > Name of Video Rental Store")
                print(" > Ex >> Random Play")
                try:
                    setup.name = input(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1
            case 2:
                print(" > Creation date of Video Rental Store")
                print(" > Ex >> 20-04-2007")
                try:
                    setup.creation_date = input(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1
            case 3:
                print(" > Video Rental Store email ")
                print(" > Ex >> @random.play")
                try:
                    setup.video_rental_store_email = input(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 4:
                print(" > Video Rental Store phone ")
                print(" > Ex >> 936666666")
                try:
                    setup.video_rental_store_phone = input(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                number += 1

            case 5:
                print(" > Street")
                print(" > Ex >> Rua João das Coves")
                setup.street = input(" >> ")

                number += 1

            case 6:
                print(" > City")
                print(" > Ex >> Lisboa")
                setup.city = input(" >> ")

                number += 1

            case 7:
                print(" > Region")
                print(" > Ex >> Grande Lisboa")
                setup.region = input(" >> ")

                number += 1

            case 8:
                print(" > Country")
                print(" > Ex >> Portugal")
                setup.country = input(" >> ")

                number += 1

    return setup


def confirm_setup(setup: Setup):
    while True:
        cls()

        print(header_confirm)

        print(setup)

        print("\n > Do you want continue in this configuration")
        print(" > [ Y | N ]")
        confirmation = input(" >> ").upper()

        if confirmation == "Y":
            print("\n > Preview")
            print(setup)
            print("\n > Configuration saved")
            create_json(VIDEO_RENTAL_STORE_PATH, setup.to_dict())
            press_to_continue()
            break

        elif confirmation == "N":
            cls()

            print(" > What do you want to change?")
            print(" [ 1 ] - Name")
            print(" [ 2 ] - Creation Date")
            print(" [ 3 ] - Video Rental Store Email")
            print(" [ 4 ] - Video Rental Store Phone")
            print(" [ 5 ] - Location")
            print(" [ 0 ] - Exit")

            try:
                change_option = catch_number_error(" >> ")

            except ValueError as error:
                print(error)
                press_to_continue()
                continue

            match change_option:
                case 1:
                    print(" > Name of Video Rental Store")
                    print(" > Ex >> Random Play")
                    try:
                        setup.name = input(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()
                        continue

                case 2:
                    print(" > Creation date of Video Rental Store")
                    print(" > Ex >> 20-04-2007")
                    try:
                        setup.creation_date = input(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()
                        continue

                case 3:
                    print(" > Video Rental Store email ")
                    print(" > Ex >> @random.play")
                    try:
                        setup.video_rental_store_email = input(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()
                        continue

                case 4:
                    print(" > Video Rental Store phone ")
                    print(" > Ex >> 936666666")
                    try:
                        setup.video_rental_store_phone = input(" >> ")

                    except ValueError as error:
                        print(error)
                        press_to_continue()
                        continue

                case 5:
                    while True:
                        cls()

                        print(" > What do you want to change?")
                        print(" [ 1 ] - Street")
                        print(" [ 2 ] - City")
                        print(" [ 3 ] - Region")
                        print(" [ 4 ] - Country")
                        print(" [ 0 ] - Exit")

                        try:
                            change_option = catch_number_error(" >> ")

                        except ValueError as error:
                            print(error)
                            press_to_continue()
                            continue

                        print(" > Location ")

                        match change_option:
                            case 1:
                                print(" > Street")
                                print(" > Ex >> Rua João das Coves")
                                setup.street = input(" >> ")

                            case 2:
                                print(" > City")
                                print(" > Ex >> Lisboa")
                                setup.city = input(" >> ")

                            case 3:
                                print(" > Region")
                                print(" > Ex >> Grande Lisboa")
                                setup.region = input(" >> ")

                            case 4:
                                print(" > Country")
                                print(" > Ex >> Portugal")
                                setup.country = input(" >> ")

                            case 0:
                                print(" > Back to confirmation")
                                press_to_continue()
                                break
                            case _:
                                print(" > [ ERROR ]")
                                print(" > Enter a validate option")
                                press_to_continue()
                                pass

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
