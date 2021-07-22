people = [
    {
    'first_name': 'Hooman',
    'last_name': 'Foroudastan',
    'age': 33,
    'city': 'Durham'
    },
    { 
    'first_name': 'John',
    'last_name': 'Smith',
    'age': 49,
    'city': 'Raleigh'
    },
    { 
    'first_name': 'Tim',
    'last_name': 'Doe',
    'age': 26,
    'city': 'Cary'
    }
]

for person in people:
    print(f"My name is {person['first_name']} {person['last_name']}. I am {person['age']}. I live in {person['city']}.")
