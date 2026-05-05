def verify_user(clients: dict, email: str):

    for client in clients["clients"]:
        if client["email"] == email:
            return client

    return None


def verify_password(client: dict, password: str):

    if client["password"] == password:
        return True

    return False
