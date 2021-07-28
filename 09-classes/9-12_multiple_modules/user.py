class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"Hello. My name is {self.first_name.title()} {self.last_name.title()}.")
        print(f"I am {self.age} in age. Also, I live in {self.location.title()}.")
    
    def greet_user(self):
        print(f"Welcome! It is nice to meet you, {self.first_name.title()}.")