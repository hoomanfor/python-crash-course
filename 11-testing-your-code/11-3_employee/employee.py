class Employee:
    def __init__(self, first_name, last_name, bonus):
        self.first_name = first_name
        self.last_name = last_name
        self.bonus = int(bonus)

    def give_bonus(self, bonus=10):
        self.bonus += int(bonus)