active = True
filename = 'programming_poll.txt'

while active:
    answer = input("Why do you like programming?\n(type 'q' to quite this program) ")
    if answer == 'q':
        active = False
    else:
        print(f'That\'s and awesome answer.')
        with open(filename, 'a') as file_object:
            file_object.write(f"Answer: {answer}\n")
