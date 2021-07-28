from random import choice

options = (5, 22, 23, 'h', 34, 'a', 'e', 'p', 'q', 982, 132, 7, 88, 93, 2)
winning_options = []
i = 1
while i <= 4:
    selected_option = choice(options)
    winning_options.append(selected_option)
    i += 1

print(f"Any ticket matching these four numbers or letters wins a prize:\n{winning_options}")
