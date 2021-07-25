def make_sandwich(*toppings):
    print("I will make you a sandwhich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('turkey', 'tomatoes')
make_sandwich('cheese', 'avocado', 'tuna')
make_sandwich('roast beef', 'cucumber', 'cheese')