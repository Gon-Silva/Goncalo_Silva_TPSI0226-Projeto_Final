from GenericUtlis.files import read_json, write_json


def save_account(client: dict):
    data = read_json("data_base/clients/clients.json")

    id = len(data["clients"]) + 1

    client["id"] = id

    data["clients"].append(client)

    write_json("data_base/clients/clients.json", data)


def check_email(clients: dict, email: str):

    for client in clients["clients"]:
        if client["email"] == email:
            return False

    return True
