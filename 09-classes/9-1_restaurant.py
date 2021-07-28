class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Welcome to '{self.restaurant_name}''. We serve {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"'{self.restaurant_name}' is open for business!")

my_restaurant = Restaurant("Hooman's Eats", "BBQ")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()