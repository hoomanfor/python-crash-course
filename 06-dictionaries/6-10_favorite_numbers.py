favorite_numbers = {
    "Hooman": [7, 10, 44],
    "Tim": [73, 55, 11],
    "John": [198, 0, 36],
    "Eric": [32, 41, 43],
    "Klara": [23, 77, 22]
}

for person, numbers in favorite_numbers.items():
    print(f"{person.title()}'s favorite numbers are the following:")
    for number in numbers:
        print(f"* {number}")