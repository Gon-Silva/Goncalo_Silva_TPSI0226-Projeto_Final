from GenericUtlis.files import read_json
from GenericUtlis.terminal import cls, press_to_continue
from Headers.headers import header_login
from Login.utils_login import verify_password, verify_user


def login():

    data_clients = read_json("data_base/clients/clients.json")
    number_of_attempts = 5

    while True:
        cls()

        print(header_login)

        if number_of_attempts == 0:
            print("Sorry, but number of attempts is end")
            press_to_continue()
            break

        email = input("Email - ")

        client = verify_user(data_clients, email)
        if client is None:
            print("\nSorry, but your email doesn't exist, please try again\n")

            number_of_attempts -= 1

            press_to_continue()
            continue

        password = input("Password - ")

        if not verify_password(client, password):
            print("\nSorry, but your password is incorrect, please try again\n")

            number_of_attempts -= 1

            press_to_continue()
            continue

        print("\nAll right\n")
        press_to_continue()
