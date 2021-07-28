class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Welcome to '{self.restaurant_name}''. We serve {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"'{self.restaurant_name}' is open for business!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number):
        self.number_served += increment_number

restaurant = Restaurant("Hooman's Eats", "BBQ")
print(restaurant.number_served)

restaurant.number_served = 23
print(restaurant.number_served)

restaurant.set_number_served(50)
print(restaurant.number_served)

restaurant.increment_number_served(20)
print(restaurant.number_served)