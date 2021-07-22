pets = [
    {'kind': 'dog', 'owner': 'hooman'},
    {'kind': 'cat', 'owner': 'john'},
    {'kind': 'fish', 'owner': 'tim'},
]

for pet in pets:
    print(f"{pet['owner'].title()} is the owner of a {pet['kind']}.")