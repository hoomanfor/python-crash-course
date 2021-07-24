sandwich_orders = ['roast beef', 'turkey', 'salami', 'tuna']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made you a {current_sandwich.title()} sandwich.")
    finished_sandwiches.append(current_sandwich)
print(f"The following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"* {sandwich.title()} Sandwich")