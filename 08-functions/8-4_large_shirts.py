def make_shirt(message='I love Python.', size='large'):
    print(f"Your shirt is size {size.title()} and the message you have included on the shirt is as follows:")
    print(f"'{message}'\n")

make_shirt()
make_shirt(size='medium')
make_shirt(message='I love JavaScript.')