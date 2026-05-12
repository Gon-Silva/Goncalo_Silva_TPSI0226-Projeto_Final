from GenericUtlis.errors import catch_number_error
from GenericUtlis.terminal import cls, press_to_continue
from Headers.headers import header_name_store
from Login.login import login
from NewAccount.new_account import new_account
from Setup.setup import setup


def main():

    while True:
        cls()

        setup()

        print(header_name_store)

        print("[1] - Login")
        print("[2] - New Account")
        print("[3] - Leave Program")

        option = catch_number_error("\nSelect an option -> ")

        if option is None:
            continue

        match option:
            case 1:
                login()
                pass
            case 2:
                new_account()
                pass
            case 3:
                print("\nThank you for using\n")
                break
            case _:
                print("\n[ERROR] Between 1 and 3")
                press_to_continue()


if __name__ == "__main__":
    main()
