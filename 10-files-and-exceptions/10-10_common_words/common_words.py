filename = "the_great_gatsby.txt"

with open(filename) as file_object:
    contents = file_object.read().lower()
    quantity = contents.count("the ")
    print(f"The word 'the' appears in '{filename}' a total of {quantity} times.")