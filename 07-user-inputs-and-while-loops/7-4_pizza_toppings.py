prompt = "\nEnter the name of a pizza topping you would like to eat:"
prompt += "\n(Type 'quite' to exit this program.) "
topping= ""
while topping != 'quite':
    topping = input(prompt)
    if topping != 'quite':
        print(f"I will add {topping.title()} to your pizza!")