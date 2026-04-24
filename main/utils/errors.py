from utils.terminal import name


def catch_number_error(message: str):
    try:
        return int(input(message))
    except ValueError:
        print("\n[ERROR] The input must be a number")
        name()
        return None
