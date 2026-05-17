# Path
from config import CLIENTS_PATH, EMPLOYEES_PATH

# My Library
from GenericUtlis.errors import catch_number_error
from GenericUtlis.files import check_file, read_json
from GenericUtlis.terminal import cls, press_to_continue


def list_all_clients() -> None:

    batch_size = 10

    cls()

    check_file(CLIENTS_PATH)
    data = read_json(CLIENTS_PATH)
    clients = data["clients"]

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
                        # Goes to the page of edit account
                        print("\n > Welcome to edit account page")
                        pass

                    case 3:
                        # Goes to the page of edit account
                        print("\n > Welcome to edit account page")
                        pass

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

