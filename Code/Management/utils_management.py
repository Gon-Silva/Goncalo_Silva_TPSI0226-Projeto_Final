# Path
from config import CLIENTS_PATH

# My Library
from GenericUtlis.algorithms import binary_search, linear_search
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
                print(" [ 2 ] - Edit Account")
                print(" [ 3 ] - Remove Account")
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

                        edit_client(client)

                    case 3:
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

                        remove_client(client)

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


def show_client(client: dict) -> None:
    print(f"\n > Client ID - {client['id']}")
    print(f"  > Name - {client['name']['first_name']} {client['name']['last_name']}")
    print(f"  > Age - {client['age']}")
    print(f"  > Email - {client['email']}")
    print(f"  > Phone - {client['phone']}")
    print(f"  > Subcription Plan - {client['subscription_plan']}")
    print(f"  > Active - {client['is_active']}")


def find_client_by_id(id: int) -> dict | None:
    clients = read_json(CLIENTS_PATH)["clients"]
    return binary_search(clients, "id", id)


def find_client_by_name(name: str) -> dict | None:
    clients = read_json(CLIENTS_PATH)["clients"]
    return linear_search(clients, "name", name)


def edit_client(client: dict) -> None:

    while True:
        cls()

        show_client(client)

        print(" > What do you want to change?")
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
                print(" > Change First Name")
                try:
                    client["name"]["first_name"] = input_name(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 2:
                print(" > Change Last Name")
                try:
                    client["name"]["last_name"] = input_name(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 3:
                print(" > Change Age")
                try:
                    client["age"] = input_age(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 4:
                try:
                    client["phone"] = input_phone(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 5:
                try:
                    client["nif"] = input_nif(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 6:
                try:
                    client["email"] = input_email_client(" >> ")

                except ValueError as error:
                    print(error)
                    press_to_continue()
                    break

            case 7:
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
                pass

            case _:
                print("\n > [ ERROR ]")
                print(" > Enter a validate option")
                press_to_continue()
                pass


def remove_client(client: dict) -> None:
    while True:
        cls()

        show_client(client)

        print(" > Do you want remove this user")
        print(" > [ Y | N ]")
        want_remove = input(" >> ").upper()

        if want_remove == "Y":
            client["is_active"] = False
            save_client(client)
            print("\n > Client removed successfully")
            press_to_continue()

        elif want_remove == "N":
            return None

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
