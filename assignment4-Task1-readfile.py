''' This program will print lines of the given file '''

file1 = 'd:\\sample.txt'

try:
    fh1 = open(file1, 'r')
    lines = fh1.readlines()
    print("Reading line content:")
    if len(lines) != 0:
        for line in lines:
            print(f"line {lines.index(line) + 1}: {line.strip()}")
        fh1.close()
    else :
        print(f"{file1} is empty")
except:
    print(f"Error: The file {file1} was not present.")
