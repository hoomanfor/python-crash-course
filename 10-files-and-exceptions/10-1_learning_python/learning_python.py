# To get this program to open 'learning_python.txt', I had to alter a VS Code Setting.
#   (i.e. Enable Python > Terminal: Execute in File Dir)

# Print the contents once by reading in the entire file.
print("\n")
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

# Print once by looping over the file object.
print("\n")
filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

# Print once by storing the lines in a list and then working with them outside the with block.
print("\n")
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
