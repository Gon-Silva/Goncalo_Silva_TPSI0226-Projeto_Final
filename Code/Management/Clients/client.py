# My Library
from GenericUtlis.errors import catch_number_error
from GenericUtlis.terminal import cls, press_to_continue
from Headers.headers import header_manage_client
from Management.utils_management import list_all_clients


def manage_client():

    while True:
        cls()

        print(header_manage_client)

        print(" > What do you want to do?")
        print(" [ 1 ] - List All Customers")
        print(" [ 2 ] - Search For a Customer")
        print(" [ 3 ] - Edit Customer")
        print(" [ 4 ] - Remove Customer")
        print(" [ 5 ] - Sort customers")
        print(" [ 6 ] - Statistics")
        print(" [ 0 ] - Back")

        try:
            option = catch_number_error("\n >> ")

        except ValueError as error:
            print(error)
            press_to_continue()
            continue

        match option:
            case 1:
                list_all_clients()

            case 2:
                print("Search For a Customer (by ID, name, email)")

            case 3:
                print("Edit Customer")

            case 4:
                print("Remove Customer")

            case 5:
                print("Sort customers")

            case 6:
                print("Statistics")

            case 0:
                print("\n > Back to page login")
                press_to_continue()
                break

            case _:
                print("\n > [ ERROR ]")
                print(" > Enter a validate option")
                press_to_continue()
                pass
