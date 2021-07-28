from random import randint

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(f"My {self.sides}-sided dice has rolled a {randint(1, self.sides)}.")

my_dice = Dice()
my_10_sided_dice = Dice(10)
my_20_sided_dice = Dice(20)
i = 1
while i <= 10:
    my_dice.roll_die()
    my_10_sided_dice.roll_die()
    my_20_sided_dice.roll_die()
    i += 1