guests = ["John", "Jack", "Tim"]
print(f"I would like to invite you to dinner, {guests[0]}.")
print(f"I would like to invite you to dinner, {guests[1]}.")
print(f"I would like to invite you to dinner, {guests[-1]}.")
print(f"Unfortunately, {guests[2]} cannot make it to dinner.")
guests[2] = "Klara"
print(f"I would like to invite you to dinner, {guests[0]}.")
print(f"I would like to invite you to dinner, {guests[1]}.")
print(f"I would like to invite you to dinner, {guests[-1]}.")
print(f"I have found a bigger table!")
guests.insert(0, "Johanna")
guests.insert(3, "Jacob")
guests.append("Walter")
print(f"I would like to invite you to dinner, {guests[0]}.")
print(f"I would like to invite you to dinner, {guests[1]}.")
print(f"I would like to invite you to dinner, {guests[2]}.")
print(f"I would like to invite you to dinner, {guests[3]}.")
print(f"I would like to invite you to dinner, {guests[4]}.")
print(f"I would like to invite you to dinner, {guests[5]}.")
print(f"Bummer! I lost the big table and only have space for 2 guests.")
print(f"I'm sorry {guests.pop()}. I'm can't invite you to dinner.")
print(f"I'm sorry {guests.pop()}. I'm can't invite you to dinner.")
print(f"I'm sorry {guests.pop()}. I'm can't invite you to dinner.")
print(f"I'm sorry {guests.pop()}. I'm can't invite you to dinner.")
print(f"{guests[0]}! You are still invited to dinner.")
print(f"{guests[1]}! You are still invited to dinner.")
del guests[0]
del guests[0]
print(f"I have used to the del Keyword to ensure that my list is now empty (i.e. '{guests}')")