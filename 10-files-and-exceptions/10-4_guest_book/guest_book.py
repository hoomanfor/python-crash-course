active = True
filename = 'guest_book.txt'

while active:
    name = input("Enter your name:\n(type 'q' to quite this program) ")
    if name == 'q':
        active = False
    else:
        print(f'It is nice to meet you, {name}.')
        with open(filename, 'a') as file_object:
            file_object.write(f"{name}\n")
