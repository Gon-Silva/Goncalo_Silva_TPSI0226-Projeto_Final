# Python library
from pathlib import Path

# My library
from GenericUtlis.files import read_json, write_json
from GenericUtlis.terminal import cls, press_to_continue



def setup():

    statement_file =  Path("DataBase/statement.py")

    if not statement_file.exists():
        return

    if 