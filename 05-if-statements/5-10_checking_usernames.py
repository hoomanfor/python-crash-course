current_users = ["hooman_dude", "john_dude", "jacob_dude", "william_dude", "jack_dude"]

new_users = ["bill_dude", "james_dude", "adam_dude", "HOOMAN_dude", "jack_DUDE"]

if new_users:
    for new_user in new_users:
        if new_user.lower() in current_users:
            print(f"Sorry {new_user}, you will need to enter a new username.")
        else:
            print(f"Congratulations! {new_user} is an available username.")