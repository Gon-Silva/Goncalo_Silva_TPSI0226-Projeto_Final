from utils.terminal import press_to_continue


def catch_number_error(message: str):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("\n[ERROR] The input must be a number")
            press_to_continue()
