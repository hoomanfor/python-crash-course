polling_active = True

def make_album(name, title, number_of_songs=None):
    if number_of_songs:
        album = {'name': name, 'title': title, 'number_of_songs': number_of_songs}
    else:
        album = {'name': name, 'title': title}
    return album


while polling_active:
    quite = "\n(Enter 'q' if you would like to quite this program.) "
    name = input(f"\nEnter the album's artist name: {quite}")
    if name == 'q':
        break
    title = input(f"\nEnter the album's title: {quite}")
    if title == 'q':
        break
    print("\nNew Dictionary Created:")
    print(make_album(name, title))