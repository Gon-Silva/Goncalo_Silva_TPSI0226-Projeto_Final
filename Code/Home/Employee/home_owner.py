# PATH

# My Library
from GenericUtlis.errors import catch_number_error
from GenericUtlis.terminal import press_to_continue
from Headers.headers import header_home_page


def home_page_owner(employee: dict):

    while True:
        print(header_home_page)

        print(f" > Welcome {employee['first_name']} {employee['last_name']}")

        print(" > What do you want do to?")
        print(" [ 1 ] - Manage Customers")
        print(" [ 2 ] - Manage Employees")
        print(" [ 3 ] - Manage Movies")
        print(" [ 4 ] - Manage Plans")
        print(" [ 5 ] - View Statistics")
        print(" [ 6 ] - Edit Account")
        print(" [ 7 ] - Edit Video Rental Store Information")
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
                print("\n > Welcome to manage clients page")
                pass

            case 2:
                # Goes to the page of manage employees
                print("\n > Welcome to manage employees page")
                pass

            case 3:
                # Goes to the page of manage movies
                print("\n > Welcome to manage movies page")
                pass

            case 4:
                # Goes to the page of manage plans
                print("\n > Welcome to manage plans page")
                pass

            case 5:
                # Goes to the page of view statistics
                print("\n > Welcome to view statistics page")
                pass

            case 6:
                # Goes to the page of edit account
                print("\n > Welcome to edit account page")
                pass

            case 7:
                # Goes to the page of edit video rental store information
                print("\n > Welcome to edit video rental store information page")
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
