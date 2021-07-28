from random import choice

options = (5, 22, 23, 'h', 34, 'a', 'e', 'p', 'q', 982, 132, 7, 88, 93, 2)
my_ticket = [22, 23, 'a', 'q']
winning_options = []
iterations = 0

def generate_winning_ticket():
    for i in range(4):
        selected_option = choice(options)
        winning_options.append(selected_option)

while my_ticket != winning_options:
    winning_options = []
    generate_winning_ticket()
    iterations += 1
    print(f"A winning ticket has been generated: #{iterations}")
    print(f"Any ticket matching these four numbers or letters wins a prize:\n{winning_options}")