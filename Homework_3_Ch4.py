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

for y in range(7,0,-1):
    for x in range(y):
        print("*", end="")
    print()

# Use a loop with the turtle graphics library to draw the star design
import turtle

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

