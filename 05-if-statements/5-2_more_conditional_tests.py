musician = "First Aid Kit"
print(f"Is musician == 'First Aid Kit'? I predict True.")
print(musician == "First Aid Kit")

print(f"Is musician == 'Fleet Foxes'? I predict False.")
print(musician == "Fleet Foxes")

print(f"Is musician.lower() == 'first aid kit'? I predict True.")
print(musician.lower() == 'first aid kit')

number = 9
print(f"Is number == 9? I predict True.")
print(number == 9)

print(f"Is number != musician? I predict True.")
print(number != musician)

print(f"Is number > 5? I predict True.")
print(number > 5)

print(f"Is number < 5? I predict False.")
print(number < 5)

print(f"Is number <= 9? I predict True.")
print(number <= 9)

print(f"Is number >= 10? I predict False.")
print(number >= 10)

print(f"Is number >= 10 and musician == 'First Aid Kit'? I predict False.")
print(number >= 10 and musician == 'First Aid Kit')

print(f"Is number >= 10 or musician == 'First Aid Kit'? I predict True.")
print(number >= 10 or musician == 'First Aid Kit')

colors = ["red", "green", "blue"]
print(f"Is 'red' in colors? I predict True.")
print('red' in colors)

colors = ["red", "green", "blue"]
print(f"Is 'red' not in colors? I predict False.")
print('red' not in colors)