def describe_city(name, country="united states"):
    print(f"{name.title()} is in {country.title()}.\n")

describe_city(name="raleigh")
describe_city(name="durham")
describe_city(name="stockholm", country="sweden")