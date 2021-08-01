def get_formatted_location(city, country, population=''):
    formatted_location = f"{city}, {country}".title()
    if population:
        formatted_location += f" - population {population}."
    return formatted_location