import json
import os


def read_json(path: str):
    try:
        with open(path, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("File not found")
        print("Create a new file")
        with open(path, "w") as file:
            data = {"clients": []}
            json.dump(data, file)
        return data


def write_json(path: str, data: dict):
    with open(path, "w") as file:
        json.dump(data, file)
