from builtins import enumerate
with open("textt.txt","r") as file:
    for line_number , line in enumerate(file,1):
        line = line.strip()
        print(f"line {line_number} : {line}")