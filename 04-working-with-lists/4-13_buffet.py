foods = ("bread", "chicken", "oatmeal", "avocado", "cheese")
print(f"The 1st iteration of the foods tuple:")
for food in foods:
  print(food)
print("\n")
# foods[0] = "chocolate" results in a TypeError: 'tuple' object does not support item assignment
foods = ("broccoli", "cauliflower", "oatmeal", "avocado", "cheese")
print(f"The 2nd iteration of the foods tuple:")
for food in foods:
  print(food)