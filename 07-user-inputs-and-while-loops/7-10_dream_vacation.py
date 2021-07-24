responses = {}
polling_active = True

while polling_active:
    name = input("\nEnter your name: ")
    response = input("\nWhere would you like to vacation to? ")
    responses[name] = response
    repeat = input("\n(Would you like to let another person respond? Type 'yes' or 'no'" )
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to vacation in {response.title()}.")