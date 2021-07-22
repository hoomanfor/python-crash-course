cities = {
    'raleigh': {
        'country': "united states",
        'population': 464485,
        'fact': 'Raleigh is the capital of North Carolina.'
    },
    'durham': {
        'country': "united states",
        'population': 269702,
        'fact': 'Durham is a part of the Research Triangle Region.'
    },
    'cary': {
        'country': "united states",
        'population': 166268,
        'fact': 'Cary is predominantly in Wake County.'
    }
}

for city, information in cities.items():
    print(f"Here's some information about the city of {city.title()}:")
    for key, value in information.items():
        if key == 'country':
            print(f"* {key.title()}: {value.title()}")
        else:
            print(f"* {key.title()}: {value}")
