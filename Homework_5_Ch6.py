# Write a program that asks the user for the name of a file. The program should display only
# the first five lines of the file’s contents. If the file contains less than five lines, it should
# display the file’s entire contents.

file_name = input("Enter the name of the file: ")

try:
    with open(file_name, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            print("{}: {}".format(line_number, line.rstrip()))
except FileNotFoundError:
    print("File not found.")
except IOError:
    print("Error reading the file.")


# In this chapter’s source code folder, you will find a text file named numbers.txt. Write a
# program that reads all of the numbers stored in the file and calculates their total.

print("We do not have access to a source code folder within this book.")
print("I was unable to find both a source code folder or a text file named numbers.txt in this book")