rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'amazon': 'peru'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(f"The {river.title()}.")

for country in rivers.values():
    print(country.title())