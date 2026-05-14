def catch_number_error(message: str):
    while True:
        try:
            return int(input(message))
        except ValueError:
            raise ValueError("\n[ERROR] The input must be a number")
