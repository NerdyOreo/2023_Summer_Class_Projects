import turtle
import math

# Write a program that displays the following information:
    #Your name
    #Your address, with city, state, and ZIP
    #Your telephone number
    #Your college major

# There are a few different ways to achieve this. The first method is below:
print("Name: Tyler Gates""\n""Address: 1600 Pennsylvania Avenue, Washington DC 20500""\n""Phone Number: (401)215-6334""\n""College Major: Cyber Security")
# The Second method is longer but allows for changes to be made on the fly without editing the print function:
name = input("Enter your First and last name:")
address = input("Enter your address:")
phone = input("Enter your Phone Number:")
major = input("Enter your Major:")
print(name, "\n", address, "\n", phone, "\n", major)

# A company has determined that its annual profit is typically 23 percent of total sales. Write
# a program that asks the user to enter the projected amount of total sales, then displays the
# profit that will be made from that amount.
# Hint: Use the value 0.23 to represent 23 percent.

projected = float(input("Enter the projected amount of total sales:"))
print("Your profit will be", round(projected*0.23, 2), "dollars")

# A customer in a store is purchasing five items. Write a program that asks for the price of
# each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

item1 = float(input("Enter the price of Item 1:"))
item2 = float(input("Enter the price of Item 2:"))
item3 = float(input("Enter the price of Item 3:"))
item4 = float(input("Enter the price of Item 4:"))
item5 = float(input("Enter the price of Item 5:"))
subtotal = item1+item2+item3+item4+item5
tax = float(subtotal) * 0.07
finaltotal = float(subtotal) + float(tax)
print("Your subtotal is: $", subtotal, "\n" "Tax will be: $", tax, "\n" "Your total after tax is: $", finaltotal)

# Write a program that asks the user to enter the amount of a purchase and the desired
# number of payment instalments. The program should add 5 percent to the amount to get
# the total purchase amount, and then divide it by the desired number of instalments, then
# display messages telling the user the total amount of the purchase and how much each
# instalment will cost.

purchase_price = float(input("Enter the amount of a purchase:"))
num_payments = int(input("Enter the desired number of payments:"))
total_p = purchase_price+(purchase_price * 0.05)
pmts = total_p/num_payments
print("The total purchase price is $", total_p, "and each payment in your", num_payments, "month long installment plan is $", pmts)


# Write a program that calculates the total amount of a meal purchased at a restaurant. The
# program should ask the user to enter the charge for the food, then calculate the amounts
# of an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

meal_base = float(input("Enter the charge for the food:"))
meal_tip = round(float(meal_base) * 0.18, 2)
meal_tax = round(float(meal_base) * 0.07, 2)
meal_total = round(meal_base+meal_tip + meal_tax, 2)
print("You are paying $", meal_tax, "in taxes and you need to leave an 18% tip, which comes out to be $", meal_tip, "The total you should be paying for this meal is: $", meal_total)


# Use the turtle graphics library to write programs that reproduce each of the designs shown
# in Figure 2-40.
# Figure 1 (Double Diamonds)
s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("blue")
t.fillcolor("white")
t.begin_fill()
t.rt(135)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(200)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.lt(90)
t.fd(100)
t.end_fill()
t.clear()

# Figure 2 (Nested Triangle)
screen = turtle.Screen()
t = turtle.Turtle()
screen.bgcolor("blue")
t.fillcolor("white")
t.begin_fill()
t.lt(180)
t.fd(200)
t.rt(110)
t.fd(292.38044)
t.rt(140)
t.fd(292.38044)
t.rt(155)
t.fd(141.42136)
t.lt(90)
t.fd(141.42136)
t.end_fill()
t.clear()

# Figure 3 ("3d" rectangle illusion)
screen = turtle.Screen()
t = turtle.Turtle()
screen.bgcolor("blue")
t.fillcolor("white")
t.begin_fill()
t.lt(180)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(135)
t.fd(282.842)
t.rt(135)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(45)
t.fd(141.421)
t.rt(135)
t.fd(200)
t.lt(135)
t.fd(141.421)
t.end_fill()
t.clear()

# Figure 4 (rings)
screen = turtle.Screen()
t = turtle.Turtle()
screen.bgcolor("blue")
t.fillcolor("white")
t.begin_fill()
t.lt(90)
t.circle(60)
t.rt(90)
t.circle(-60)
t.penup()
t.goto(130, 0)
t.pendown()
t.lt(90)
t.circle(60)
t.rt(90)
t.circle(-60)
t.penup()
t.goto(260, 0)
t.pendown()
t.lt(90)
t.circle(60)
t.end_fill()
t.clear()


# Figure 5 (graph)
screen = turtle.Screen()
t = turtle.Turtle()
screen.bgcolor("blue")
t.fillcolor("white")
t.begin_fill()
t.penup()
t.goto(0, -50)
t.pendown()
t.circle(50)
t.penup()
t.goto(0, 0)
t.pendown()
t.fd(250)
t.penup()
t.goto(0, 0)
t.pendown()
t.lt(90)
t.fd(250)
t.penup()
t.goto(0, 0)
t.pendown()
t.lt(90)
t.fd(250)
t.penup()
t.goto(0, 0)
t.pendown()
t.lt(90)
t.fd(250)
t.penup()
t.goto(0, 0)
t.pendown()
t.end_fill()
t.clear()


# Write a program that asks the user to enter an integer. The program should display
# “Positive” if the number is greater than 0, “Negative” if the number is less than 0, and
# “Zero” if the number is equal to 0. The program should then display “Even” if the number
# is even, and “Odd” if the number is odd.

posneg = int(input("Enter an integer:"))
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

# A bug collector collects bugs every day for five days. Write a program that keeps a running
# total of the number of bugs collected during the five days. The loop should ask for the
# number of bugs collected for each day, and when the loop is finished, the program should
# display the total number of bugs collected.

total_bugs = 0

for day in range(1, 6):
    bugs = int(input("Input how many bugs were collected today: "))
    total_bugs += bugs

print("The total number of bugs collected over the last 5 days is:", total_bugs)


# Running on a particular treadmill you burn 4.2 calories per minute. Write a program that
# uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.

minutes = [10, 15, 20, 25, 30]

for number in minutes:
    calories_burned = number * 4.2
    print('You burned {} calories in {} minutes'.format(calories_burned, number))


# Write a program that calculates the amount of money a person would earn over a period
# of time if his or her salary is one penny the first day, two pennies the second day, and
# continues to double each day. The program should ask the user for the number of days.
# Display a table showing what the salary was for each day, then show the total pay at the
# end of the period. The output should be displayed in a dollar amount, not the number of
# pennies.

pennies = 1
inpdays = int(input("Enter the total number of days: "))
total_earned = 0

for cnt in range(1, inpdays + 1):
    pennies *= 2
    total_earned += pennies / 100
    print('Day', cnt, 'Pay', pennies / 100)

print('You earned a total of ${:.2f}'.format(total_earned))


# Write a program with a loop that asks the user to enter a series of positive numbers. The
# user should enter a negative number to signal the end of the series. After all the positive
# numbers have been entered, the program should display their sum.

total_sum = int(input("Please enter the first number: "))

while True:
    user_num = int(input("Please enter the next number. To exit, enter a negative integer: "))

    if user_num >= 0:
        total_sum += user_num
    else:
        print('Your Total Sum is {}'.format(total_sum))
        break

# Write a program that uses nested loops to draw this pattern

for y in range(7, 0, -1):
    for x in range(y):
        print("*", end="")
    print()

# Use a loop with the turtle graphics library to draw the star design

remaining = 8
screen = turtle.Screen()
screen.bgcolor("blue")
turtle.fillcolor("white")
turtle.begin_fill()

while remaining > 0:
    turtle.fd(400)
    turtle.lt(135)
    remaining -= 1

turtle.end_fill()
turtle.done()


# Many financial experts advise that property owners should insure their homes or buildings
# for at least 80 percent of the amount it would cost to replace the structure. Write a program
# that asks the user to enter the replacement cost of a building, then displays the minimum
# amount of insurance he or she should buy for the property.
replacement_cost = float(input("Enter the replacement cost of the structure: "))
minimum_insurance_amount = replacement_cost * 0.80
print("The minimum amount of insurance you should buy for the property is ${:.2f}".format(minimum_insurance_amount))


# Write a program that asks the user to enter the monthly costs for the following expenses
# incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
# maintenance. The program should then display the total monthly cost of these expenses,
# and the total annual cost of these expenses.

expenses = ["Loan Payment", "Insurance", "Gas", "Oil", "Tire Maintenance", "Maintenance"]
total_monthly_cost = 0

for expense in expenses:
    cost = float(input("Enter the monthly cost for {}: ".format(expense)))
    total_monthly_cost += cost

total_annual_cost = total_monthly_cost * 12
print("The total monthly cost of these expenses is ${:.2f} and the total annual cost of these expenses is ${:.2f}".format(total_monthly_cost, total_annual_cost))

# Write a program that asks the user to enter five test scores. The program should display a
# letter grade for each score and the average test score
total_score = 0

for tst_num in range(1, 6):
    tst = float(input("Enter the grade for test number {}: ".format(tst_num)))
    total_score += tst

    if 90 <= tst <= 100:
        grade = 'A'
    elif 80 <= tst <= 89:
        grade = 'B'
    elif 70 <= tst <= 79:
        grade = 'C'
    elif 60 <= tst <= 69:
        grade = 'D'
    elif 0 <= tst <= 59:
        grade = 'F'
    else:
        print("ERROR: Not a possible score! Try again")
        continue

    print("You got a {} on Test {}".format(grade, tst_num))

average_score = total_score / 5
print("Your average test score is {:.2f}".format(average_score))

# Write a program that uses turtle graphics to display a snowman, similar to the one shown
# in Figure 5-30

# Draw the snowman body
color = "grey"
screen = turtle.Screen()
screen.bgcolor("blue")
turtle.pencolor(color)
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.fillcolor(color)
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()
turtle.goto(0, -25)
turtle.pendown()
turtle.fillcolor(color)
turtle.begin_fill()
turtle.circle(75)
turtle.end_fill()
turtle.penup()
turtle.goto(0, 115)
turtle.pendown()
turtle.fillcolor(color)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()
turtle.penup()

# Eyes
turtle.goto(-15, 175)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
turtle.goto(15, 175)
turtle.pendown()
turtle.fillcolor("white")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

# Mouth
turtle.penup()
turtle.goto(-15, 155)
turtle.pendown()
turtle.pencolor("black")
turtle.fd(30)
turtle.penup()

# Hat
turtle.pencolor("black")
turtle.goto(-40, 200)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.fd(80)
turtle.lt(90)
turtle.fd(15)
turtle.lt(90)
turtle.fd(20)
turtle.rt(90)
turtle.fd(50)
turtle.lt(90)
turtle.fd(40)
turtle.lt(90)
turtle.fd(50)
turtle.rt(90)
turtle.fd(20)
turtle.rt(90)
turtle.fd(15)
turtle.end_fill()

# Arms:
turtle.pencolor()
turtle.goto(-75, 65)
turtle.pendown()
turtle.lt(90)
turtle.fd(75)
turtle.rt(45)
turtle.fd(35)
turtle.rt(35)
turtle.fd(20)
turtle.rt(180)
turtle.fd(20)
turtle.rt(90)
turtle.fd(20)
turtle.rt(145)
turtle.penup()
turtle.goto(75, 65)
turtle.pendown()
turtle.fd(75)
turtle.lt(45)
turtle.fd(20)
turtle.rt(180)
turtle.fd(20)
turtle.lt(90)
turtle.fd(20)
turtle.penup()
turtle.delay(4)

# Write a turtle graphics program that uses the square function presented in this chapter,
# along with a loop (or loops) to draw the checkerboard pattern shown in Figure 5-32.

def square(size, color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()


square_size = 50

turtle.speed(0)
turtle.penup()
turtle.goto(150, 100)
turtle.pendown()

for row in range(5):
    for col in range(5):
        if (row + col) % 2 == 0:
            square(square_size, "black")
        else:
            square(square_size, "white")
        turtle.forward(square_size)
    turtle.backward(square_size * 5)
    turtle.right(90)
    turtle.forward(square_size)
    turtle.left(90)

turtle.hideturtle()
turtle.done()

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

# Design a program that uses a loop to build a list named valid_numbers that contains only
# the numbers between 0 and 100 from the numbers list below. The program should then
# determine and display the total and average of the values in the valid_numbers list.
# numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

numbers = [74, 19, 105, 20, -2, 67, 7, 124, -45, 38]
total_num = 0
int_numbers = list(map(float, numbers))
valid_numbers = []
for picked_numbers in int_numbers:
    if 0 <= picked_numbers <= 100:
        total_num += picked_numbers
        valid_numbers.append(picked_numbers)
    else:
        continue
total_val_num = len(valid_numbers)
average_num = total_num / total_val_num
print("The list of total valid numbers is: {}".format(valid_numbers))
print("The total of the values in the list is {}".format(total_num))
print("The average of the values in the list is: {}".format(average_num))



# Design a program that lets the user enter the total rainfall for each of 12 months into a
# list. The program should calculate and display the total rainfall for the year, the average
# monthly rainfall, the months with the highest and lowest amounts.
def rainfall_statistics():
    rainfall_data = []

    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall (in inches) for month {month}: "))
        rainfall_data.append(rainfall)

    total_rainfall = sum(rainfall_data)

    average_rainfall = total_rainfall / 12

    highest_rainfall = max(rainfall_data)
    lowest_rainfall = min(rainfall_data)
    highest_months = [i + 1 for i, rainfall in enumerate(rainfall_data) if rainfall == highest_rainfall]
    lowest_months = [i + 1 for i, rainfall in enumerate(rainfall_data) if rainfall == lowest_rainfall]

    print("\nRainfall Statistics")
    print("-------------------")
    print("Total rainfall for the year {:.2f}".format(total_rainfall))
    print("Average monthly rainfall: {:.2f} inches".format(average_rainfall))
    print("Month {} had the highest rainfall at ({} inches)".format(', '.join(map(str, highest_months)), highest_rainfall))
    print("Month {} had the lowest rainfall at ({} inches)".format(', '.join(map(str, lowest_months)), lowest_rainfall))

rainfall_statistics()





# If you have downloaded the source code, you will find the following files in the Chapter 07
# folder:
#       • GirlNames.txt This file contains a list of the 200 most popular names given to girls
#         born in the United States from the year 2000 through 2009.
#       • BoyNames.txt This file contains a list of the 200 most popular names given to boys
#         born in the United States from the year 2000 through 2009.
# Write a program that reads the contents of the two files into two separate lists. The user
# should be able to enter a boy’s name, a girl’s name, or both, and the application will display
# messages indicating whether the names were among the most popular.

print("We do not have access to a source code folder within this book.")
print("I was unable to find both a source code folder or  text files named GirlNames.txt and BoyNames.txt in this book")





# The Lo Shu Magic Square is a grid with 3 rows and 3 columns, shown in Figure 7-21. The
# Lo Shu Magic Square has the following properties:
#       • The grid contains the numbers 1 through 9 exactly.
#       • The sum of each row, each column, and each diagonal all add up to the same number.
#         This is shown in Figure 7-22.
# In a program you can simulate a magic square using a two-dimensional list. Write a
# function that accepts a two-dimensional list as an argument and determines whether
# the list is a Lo Shu Magic Square. Test the function in a program.

def is_lo_shu_magic_square():
    square = []
    print("Enter a 3x3 grid of numbers:")
    for _ in range(3):
        row = input().split()
        square.append([int(num) for num in row])

    if len(square) != 3:
        return False

    for row in square:
        if len(row) != 3:
            return False

    target_sum = sum(square[0])

    for row in square:
        if sum(row) != target_sum:
            return False

    for col in range(3):
        col_sum = sum(square[row][col] for row in range(3))
        if col_sum != target_sum:
            return False

    diagonal_sum1 = sum(square[i][i] for i in range(3))
    diagonal_sum2 = sum(square[i][2 - i] for i in range(3))
    if diagonal_sum1 != target_sum or diagonal_sum2 != target_sum:
        return False

    return True

if is_lo_shu_magic_square():
    print("The given list is a Lo Shu Magic Square.")
else:
    print("The given list is not a Lo Shu Magic Square.")
