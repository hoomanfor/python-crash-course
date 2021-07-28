from user import User

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