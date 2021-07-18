my_pizzas = ["cheese", "pepperoni", "mushroom"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("chicken")
friend_pizzas.append("pineapple")
print(f"My favorite pizzas are:")
for pizza in my_pizzas:
  print(f"* {pizza}")
print(f"My friend's favorite pizzas are:")
for pizza in friend_pizzas:
  print(f"* {pizza}")