class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"Welcome to '{self.restaurant_name}''. We serve {self.cuisine_type}.")
    
    def open_restaurant(self):
        print(f"'{self.restaurant_name}' is open for business!")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'strawberry', 'chocolate']

    def list_flavors(self):
        print("Our inventory of ice cream flavors are as follows:")
        for flavor in self.flavors:
            print(f"* {flavor.title()}")

my_restaurant = IceCreamStand('Sweet Ice Cream Shop', 'Dessert')
my_restaurant.list_flavors()