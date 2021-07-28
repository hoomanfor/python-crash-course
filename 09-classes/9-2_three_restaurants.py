class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Welcome to '{self.restaurant_name}'. We serve {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"'{self.restaurant_name}' is open for business!")

restaurant_a = Restaurant("Hooman Eats", "BBQ")
restaurant_a.describe_restaurant()

restaurant_b = Restaurant("Japanese Eats", "Sushi")
restaurant_b.describe_restaurant()

restaurant_c = Restaurant("Mexican Eats", "Mexican")
restaurant_c.describe_restaurant()