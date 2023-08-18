import math

# Write a program that asks the user to enter an integer. The program should display
# “Positive” if the number is greater than 0, “Negative” if the number is less than 0, and
# “Zero” if the number is equal to 0. The program should then display “Even” if the number
# is even, and “Odd” if the number is odd.

posneg=int(input("Enter an integer:"))
if posneg > 0:
    if(posneg % 2) == 0:
        print("{} is a positive even number!".format(posneg))
    else:
        print("{} is a positive odd number!".format(posneg))
elif posneg == 0:
    print("{} is Zero".format(posneg))
else:
    if (posneg % 2) == 0:
        print("{} is a negative even number!".format(posneg))
    else:
        print("{} is a negative odd number!".format(posneg))


# The area of a rectangle is the rectangle’s length times its width. Write a program that asks
# for the length and width of two rectangles. The program should tell the user which
# rectangle has the greater area, or if the areas are the same.

r1l = float(input("Enter the Length of rectangle 1: "))
r1w = float(input("Enter the Width of rectangle 1: "))
r2l = float(input("Enter the Length of rectangle 2: "))
r2w = float(input("Enter the Width of rectangle 2: "))

r1a = r1l * r1w
r2a = r2l * r2w

if r1a > r2a:
    print("Rectangle 1 has a greater area than rectangle 2. Its area is", r1a)
elif r1a < r2a:
    print("Rectangle 2 has a greater area than rectangle 1. Its area is", r2a)
else:
    print("The area of the two rectangles is equal. Their areas are", r1a)



# Write a program that asks the user for a month as a number between 1 and 12. The program
# should display a message indicating whether the month is in the first quarter, the second
# quarter, the third quarter, or the fourth quarter of the year.
while True:
    month = int(input("Please enter the month you were born as a number: "))

    if month in range(1, 4):
        print("You were born in the first quarter of the year!")
        break
    elif month in range(4, 7):
        print("You were born in the second quarter of the year!")
        break
    elif month in range(7, 10):
        print("You were born in the third quarter of the year!")
        break
    elif month in range(10, 13):
        print("You were born in the fourth quarter of the year!")
        break
    else:
        print("ERROR, please try again!")



# Write a program that prompts the user to enter their points for both tests and the main
# exam and converts the values to integers. The program should first check if the points
# entered for the tests and main exam are valid. If any of the test scores are not between 0 and
# 25 or the main exam score is not between 0 and 50, the program should display an error
# message. Otherwise, the program should display the total points and the grade.
while True:
    test1 = int(input("Enter your grade from Test 1: "))
    test2 = int(input("Enter your grade from Test 2: "))
    exam = int(input("Enter your grade from the Exam: "))

    if test1 < 0 or test1 > 25 or test2 < 0 or test2 > 25 or exam < 0 or exam > 50:
        print("ERROR, Try Again")
        continue

    grade = test1 + test2 + exam

    if grade < 50 or exam < 25:
        print("You have failed the class! You got a {}.".format(grade))
        break
    elif grade > 80:
        print("You passed the class and received a Distinction! You got a {}!".format(grade))
        break
    elif 60 <= grade <= 80:
        print("You have passed the class and received a Credit! You got a {}!".format(grade))
        break
    else:
        print("You have passed the class and received a Pass. You got a {}.".format(grade))
        break

# Write a program that calculates the number of packages of hot dogs
# and the number of packages of hot dog buns needed for a cookout,
# with the minimum amount of leftovers

people = int(input("Enter how many people will be attending the cookout: "))
hotdogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

total_hotdogs = people * hotdogs_per_person
hotdog_packages = math.ceil(total_hotdogs / 10)
buns_packages = math.ceil(total_hotdogs / 8)

leftover_hotdogs = (10 * hotdog_packages) - total_hotdogs
leftover_buns = (8 * buns_packages) - total_hotdogs

print("The minimum number of packages of hot dogs required:", hotdog_packages)
print("The minimum number of packages of hot dog buns required:", buns_packages)
print("The number of hot dogs that will be left over:", leftover_hotdogs)
print("The number of hot dog buns that will be left over:", leftover_buns)
