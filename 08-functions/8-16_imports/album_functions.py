def make_album(name, title, number_of_songs=None):
    if number_of_songs:
        album = {'name': name, 'title': title, 'number_of_songs': number_of_songs}
    else:
        album = {'name': name, 'title': title}
    return album