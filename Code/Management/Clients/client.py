# My Library
from GenericUtlis.errors import catch_number_error
from GenericUtlis.terminal import cls, press_to_continue
from Headers.headers import header_manage_client
from Management.utils_management import (
    edit_client,
    find_client_by_id,
    list_all_clients,
    search_for_customer,
    select_client_by_id,
)


def manage_client():

    while True:
        cls()

        print(header_manage_client)

        print(" > What do you want to do?")
        print(" [ 1 ] - List All Customers")
        print(" [ 2 ] - Search For a Customer")
        print(" [ 3 ] - Sort customers")
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
                search_for_customer()

            case 5:
                print("Sort customers")

            case 0:
                print("\n > Back to page login")
                press_to_continue()
                break

            case _:
                print("\n > [ ERROR ]")
                print(" > Enter a validate option")
                press_to_continue()
                pass
