import turtle

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
