favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

poll_candidates = ['hooman', 'tim', 'sarah', 'bill', 'edward']

for name in poll_candidates:
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll, {name.title()}.")
    else:
        print(f"I invite you to take the poll, {name.title()}.")