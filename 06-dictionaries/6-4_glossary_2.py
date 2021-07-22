glossary = {
    'dictionary': 'In Python, a "Dictionary" is a collection of key-value pairs.',
    'key-value pair': 'In Python, a "Key-Value Pair" is a set of values associated with each other.',
    'conditional test': 'In Python, a "Conditional Test" is an expression that can be evaluated to True or False.',
    'list': 'In Python, a "List" is a collection of items in a particular order.',
    'traceback': 'In Python, a "Traceback" is  a record of where the interpreter ran into trouble when trying to execute your code.',
    'set': 'In Python, a "set" is a collection in which each item must be unique.',
    'items() method': 'In Python, the "items()" method returns a list of key-value pairs.',
    'keys() method': 'In Python, the "keys()" method is useful when you don\'t need to work with all of the values in a dictionary.',
    'values() method': 'In Python, the "values()" method can be used to return a list of values without any keys.',
    'sorted() function': 'In Python, you can use the "sorted()" function to return a sorted list of the specified iterable object.'
}

for term, definition in glossary.items():
    print(f"{term.title()}:")
    print(f"{definition}\n")