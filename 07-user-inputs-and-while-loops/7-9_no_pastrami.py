sandwich_orders = ['roast beef', 'pastrami', 'turkey', 'salami', 'pastrami', 'tuna', 'pastrami']

print("The deli has run out of Pastrami sandwiches.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
