# Path
from config import CLIENTS_PATH

# My Library
from GenericUtlis.algorithms import binary_search, linear_search_name
from GenericUtlis.errors import catch_number_error
from GenericUtlis.files import check_file, read_json, write_json
from GenericUtlis.input import (
    input_age,
    input_email_client,
    input_name,
    input_nif,
    input_password,
    input_phone,
)
from GenericUtlis.terminal import cls, press_to_continue


def list_all_clients() -> None:

    batch_size = 10

    cls()

    check_file(CLIENTS_PATH)
    clients = read_json(CLIENTS_PATH)["clients"]

    total = len(clients)

    if total == 0:
        print(" > No clients found")
        press_to_continue()
        return

    start = 0

    while start < total:
        end = min(start + batch_size, total)

        cls()
        print(f" > Clients {start + 1} to {end} of {total}")

        for i in range(start, end):
            show_client(clients[i])

        if end <= total:
            print(f"\n > Showing {batch_size} clients at a time")
            print(f" > {total - end} clients remaining\n")

            while True:
                print(" > Select a option to continue")
                print(" [ 1 ] - Continue")
                print(" [ 2 ] - Modify Account")
                print(" [ 0 ] - Leave")

                try:
                    choice = catch_number_error("\n >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    continue

                match choice:
                    case 1:
                        break

                    case 2:
                        select_client_by_id()

                    case 0:
                        print("\n > Back to page login")
                        press_to_continue()
                        return

                    case _:
                        print("\n > [ ERROR ]")
                        print(" > Enter a validate option")
                        press_to_continue()
                        pass

        start = end

    print("\n > All clients displayed!")
    print(f" > Total: {total} clients")
    press_to_continue()


def search_for_customer() -> None:

    while True:
        cls()

        print(" > Search For a Customer")
        print(" [ 1 ] - ID")
        print(" [ 2 ] - Name")
        print(" [ 0 ] - Back")

        try:
            option = catch_number_error("\n >> ")

        except ValueError as error:
            print(error)
            press_to_continue()
            continue

        match option:
            case 1:
                select_client_by_id()

            case 2:
                select_client_by_name()

            case 0:
                print("\n > Back to manage client page")
                press_to_continue()
                break

            case _:
                print("\n > [ ERROR ]")
                print(" > Enter a validate option")
                press_to_continue()
                pass


def show_client(client: dict) -> None:
    print(f"\n > Client ID - {client['id']}")
    print(f"  > Name - {client['name']['first_name']} {client['name']['last_name']}")
    print(f"  > Age - {client['age']}")
    print(f"  > Nif - {client['nif']}")
    print(f"  > Email - {client['email']}")
    print(f"  > Phone - {client['phone']}")
    print(f"  > Subcription Plan - {client['subscription_plan']}")
    print(f"  > Active - {client['is_active']}")


def modify_menu(client: dict) -> None:
    while True:
        cls()

        show_client(client)

        print("\n > Select a option to continue")
        print(" [ 1 ] - Edit")
        print(" [ 2 ] - Disable")
        print(" [ 3 ] - Activate")
        print(" [ 4 ] - Delete")
        print(" [ 0 ] - Back")

        try:
            option = catch_number_error("\n >> ")

        except ValueError as error:
            print(error)
            press_to_continue()
            continue

        match option:
            case 1:
                edit_client(client)

            case 2:
                disable_client(client)

            case 3:
                activate_account(client)

            case 4:
                delete_account(client)

            case 0:
                print("\n > Back to page login")
                press_to_continue()
                break

            case _:
                print("\n > [ ERROR ]")
                print(" > Enter a validate option")
                press_to_continue()
                pass


def select_client_by_id() -> None:
    while True:
        print("\n > Select an id")
        try:
            id = catch_number_error(" >> ")

        except ValueError as error:
            print(error)
            press_to_continue()
            continue

        client = find_client_by_id(id)

        if client is None:
            print("\n > Sorry but this id doesn't exist")
            press_to_continue()
            continue

        modify_menu(client)
        break


def select_client_by_name() -> None:
    while True:
        cls()

        print("\n Enter a name")
        try:
            name = input_name(" >> ")

        except ValueError as error:
            print(error)
            press_to_continue()
            continue

        clients = find_client_by_name(name)

        if clients is None:
            print("\n > Sorry but this name doesn't exist")
            press_to_continue()
            continue

        for client in clients:
            show_client(client)

        select_client_by_id()
        break


def find_client_by_id(id: int) -> dict | None:
    clients = read_json(CLIENTS_PATH)["clients"]
    return binary_search(clients, "id", id)


def find_client_by_name(name: str) -> list | None:
    clients = read_json(CLIENTS_PATH)["clients"]
    return linear_search_name(clients, name, "name")


def edit_client(client: dict) -> None:

    while True:
        cls()

        show_client(client)

        print("\n > What do you want to change?")
        print(" [ 1 ] - Fisrt Name")
        print(" [ 2 ] - Last Name")
        print(" [ 3 ] - Age")
        print(" [ 4 ] - Phone")
        print(" [ 5 ] - NIF")
        print(" [ 6 ] - Email")
        print(" [ 7 ] - Password")
        print(" [ 8 ] - Subscription Plan")
        print(" [ 0 ] - Exit ")

        try:
            change_option = catch_number_error("\n >> ")

        except ValueError as error:
            print(error)
            press_to_continue()
            continue

        match change_option:
            case 1:
                print("\n > Change First Name")
                try:
                    client["name"]["first_name"] = input_name(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 2:
                print("\n > Change Last Name")
                try:
                    client["name"]["last_name"] = input_name(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 3:
                print("\n > Change Age")
                try:
                    client["age"] = input_age(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 4:
                print("\n > Change Phone")
                try:
                    client["phone"] = input_phone(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 5:
                print("\n > Change Nif")
                try:
                    client["nif"] = input_nif(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 6:
                print("\n > Change Email")
                try:
                    client["email"] = input_email_client(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 7:
                print("\n > Change Password")
                try:
                    client["password"] = input_password(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 8:
                print(" > In development")
                press_to_continue()

            case 0:
                print("\n > Back to confirmation")
                save_client(client)
                print("\n > Client edit successfully")
                press_to_continue()
                break

            case _:
                print("\n > [ ERROR ]")
                print(" > Enter a validate option")
                press_to_continue()
                pass


def disable_client(client: dict) -> None:
    while True:
        cls()

        show_client(client)

        print("\n > Do you want disable this user")
        print(" > [ Y | N ]")
        want_disable = input(" >> ").upper()

        if want_disable == "Y":
            client["is_active"] = False
            save_client(client)
            print("\n > Client disabled successfully")
            press_to_continue()
            break

        elif want_disable == "N":
            break

        else:
            print("\n > [ ERROR ]")
            print(" > Enter a validate option")
            press_to_continue()


def activate_account(client: dict) -> None:
    while True:
        cls()

        show_client(client)

        print("\n > Do you want activate this user")
        print(" > [ Y | N ]")
        want_activate = input(" >> ").upper()

        if want_activate == "Y":
            client["is_active"] = True
            save_client(client)
            print("\n > Client activated successfully")
            press_to_continue()
            break

        elif want_activate == "N":
            break

        else:
            print("\n > [ ERROR ]")
            print(" > Enter a validate option")
            press_to_continue()


def delete_account(client: dict) -> None:
    db = read_json(CLIENTS_PATH)
    clients_list = db["clients"]

    while True:
        cls()

        show_client(client)

        print("\n > Do you want delete this user")
        print(" > [ Y | N ]")
        want_remove = input(" >> ").upper()

        if want_remove == "Y":
            client_id = client["id"]

            updated_clients = []

            for clt in clients_list:
                if clt["id"] != client_id:
                    updated_clients.append(clt)

            db["clients"] = updated_clients

            write_json(CLIENTS_PATH, db)
            print("\n > Client removed successfully")
            press_to_continue()
            break

        elif want_remove == "N":
            break

        else:
            print("\n > [ ERROR ]")
            print(" > Enter a validate option")
            press_to_continue()


def save_client(client: dict) -> None:
    # Read the current client database from the JSON file
    clients_db = read_json(CLIENTS_PATH)

    # Iterate through all stored clients to find a matching ID
    for i, o in enumerate(clients_db["clients"]):
        # Check if the current client's ID matches the incoming client's ID
        if o["id"] == client["id"]:
            # Replace the existing client record with the new data
            clients_db["clients"][i] = client
            # Exit the loop once we've found and updated the client
            break

    # Write the updated database back to the JSON file
    write_json(CLIENTS_PATH, clients_db)
