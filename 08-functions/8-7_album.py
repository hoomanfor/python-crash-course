def make_album(name, title, number_of_songs=None):
    if number_of_songs:
        album = {'name': name, 'title': title, 'number_of_songs': number_of_songs}
    else:
        album = {'name': name, 'title': title}
    return album

print(make_album('first aid kit', 'ruins'))
print(make_album('first aid kit', "the lion's roar"))
print(make_album('joanna newsom', 'ys'))
print(make_album('joanna newsom', 'have one on me', 18))