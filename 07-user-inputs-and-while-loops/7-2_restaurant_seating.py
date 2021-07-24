quantity = input("How many people are in your dinner group?")
quantity = int(quantity)
if quantity > 8:
    print(f"Because you have {quantity} members in your dinner group, you will need to wait to be seated.")
else:
    print(f"Your table is ready!")