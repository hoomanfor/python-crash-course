def city_country(city, country):
    city_and_country = f"{city.title()}, {country.title()}"
    return city_and_country

print(city_country("Raleigh", "United States"))
print(city_country("durham", "united states"))
print(city_country("stockholm", "sweden"))
