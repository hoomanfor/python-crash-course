favorite_places = {
    'hooman': ['home', 'work', 'rtp'],
    'john': ['best buy', 'wendy\'s', 'gym'],
    'tim': ['mall', 'post office', 'park']
}

for person, places in favorite_places.items():
    print(f"{person.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

