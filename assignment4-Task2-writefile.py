''' This program will take the lines as a user input and then print lines of the given file '''

file1 = 'd:\\sample.txt'

user_input = "\n" + input("Enter the lines : ")

fh_write = open(file1, 'a')
fh_write.writelines(user_input)
fh_write.close()

try:
    fh_open = open(file1, 'r')
    lines = fh_open.readlines()
    print("Reading line content:")
    if len(lines) != 0:
        for line in lines:
            print(f"{lines.index(line) + 1} : {line.strip()}")
        fh_open.close()
    else :
        print(f"{file1} is empty")
except:
    print(f"Error: The file {file1} was not present.")
