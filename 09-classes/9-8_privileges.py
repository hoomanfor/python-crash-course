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

class Privileges:
    def __init__(self, privileges=None):
        self.privileges = ['cad add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        print("This is a list of your privileges:")
        for privilege in self.privileges:
            print(f"* {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()

admin = Admin('hooman', 'foroudastan', 33, 'durham')
admin.privileges.show_privileges()