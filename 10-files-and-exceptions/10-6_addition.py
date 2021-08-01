while True:
    first_number = input("Enter a number:\nEnter 'q' to quite. ")
    if first_number == 'q':
        break
    second_number = input("Enter a second number:\nEnter 'q' to quite. ")
    if second_number == 'q':
        break
    try:
        total = int(first_number) + int(second_number)
    except ValueError:
        print("You did not enter a number!")
    else:
        print(f"The sum of {first_number} & {second_number} is {total}.")