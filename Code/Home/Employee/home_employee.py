# PATH

# My Library
from GenericUtlis.errors import catch_number_error
from GenericUtlis.terminal import press_to_continue
from Headers.headers import header_home_page


def home_page_employee(employee: dict):

    while True:
        print(header_home_page)

        print(f" > Welcome {employee['first_name']} {employee['last_name']}")

        print(" > What do you want do to?")
        print(" [ 1 ] - See Customers")
        print(" [ 2 ] - Manage Movies")
        print(" [ 3 ] - Edit Account")
        print(" [ 0 ] - Back")

        try:
            option = catch_number_error("\n >> ")

        except ValueError as error:
            print(error)
            press_to_continue()
            continue

        match option:
            case 1:
                # Goes to the page of manage clients
                print("\n > Welcome to view clients page")
                pass

            case 2:
                # Goes to the page of manage movies
                print("\n > Welcome to manage movies page")
                pass

            case 3:
                # Goes to the page of edit account
                print("\n > Welcome to edit account page")
                pass

            case 0:
                print("\n > Back to page login")
                press_to_continue()
                pass

            case _:
                print("\n > [ ERROR ]")
                print(" > Enter a validate option")
                press_to_continue()
                pass

        print(" > In development")
        press_to_continue()
        break
