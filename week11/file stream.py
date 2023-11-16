with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
# Open a file in write mode
with open('example.txt', 'w') as file:
    # Write a single line
    file.write('Hello, this is a new line.\n')

    # Write multiple lines
    lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
    file.writelines(lines)

# Appending to a file
with open('example.txt', 'a') as file:
    file.write('This line is appended.\n')
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

