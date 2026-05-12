with open("notes.txt", "r") as file:
    lines = file.readlines()   # ['Hello, world!\n', 'This is line 2.\n']

print(lines[0].strip())        # Hello, world!