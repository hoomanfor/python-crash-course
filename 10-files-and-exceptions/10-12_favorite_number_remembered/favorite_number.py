import json
from os import read

filename = "favorite_number.json"

def read_favorite_number():
    try:
        with open(filename) as file_object:
            favorite_number = json.load(file_object)
    except FileNotFoundError:
        print(f"I know your favorite number! It's {write_favorite_number()}.")
    else:
        print(f"I know your favorite number! It's {favorite_number}.")
        
def write_favorite_number():
    favorite_number = int(input("Enter your favorite number: "))
    with open(filename, 'w') as file_object:
        json.dump(favorite_number, file_object)
        return favorite_number

read_favorite_number()