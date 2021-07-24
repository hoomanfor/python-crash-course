active = True
prompt = "\nWelcome to the movies! What is your age?"
prompt += "\n(Type 'quite' to end the program.) "
while active:
    age = input(prompt)
    if age == 'quite':
        break
    age = int(age)
    if age < 3:
        print(f"You have stated that your age is {age}. Your ticket is free.")
        active = False
    elif age < 12:
        print(f"You have stated that your age is {age}. Your ticket costs $10.")
        active = False
    else:
        print(f"You have stated that your age is {age}. Your ticket costs $15.")
        active = False