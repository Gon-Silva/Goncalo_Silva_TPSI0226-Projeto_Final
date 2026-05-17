from GenericUtlis.terminal import cls, press_to_continue
from Headers.headers import header_login
from Home.Employee.utils_home import home_page
from Login.utils_login import is_employee, verify_password, verify_user


def login():
    number_of_attempts = 5

    while True:
        cls()

        print(header_login)

        if number_of_attempts == 0:
            print("Sorry, but number of attempts is end")
            press_to_continue()
            break

        print(" > Email")
        email = input(" >> ")

        client = verify_user(email)
        if client is None:
            print("\nSorry, but your email doesn't exist, please try again\n")

            number_of_attempts -= 1

            press_to_continue()
            continue

        print("\n > Password")
        password = input(" >> ")

        if not verify_password(client, password):
            print("\nSorry, but your password is incorrect, please try again\n")

            number_of_attempts -= 1

            press_to_continue()
            continue

        if is_employee(email):
            home_page(client)

        else:
            # Goes to the page of client
            print("\n > Welcome to client page")

        print(" > In development")
        press_to_continue()
        break
