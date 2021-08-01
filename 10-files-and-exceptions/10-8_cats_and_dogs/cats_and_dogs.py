filenames = ['cats.txt', 'dog.txt']

for filename in filenames:
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print(f"Unable to locate the file named: '{filename}'")
    else:
        print(f"Reading the contents of '{filename}':")
        print(f"{contents}\n")