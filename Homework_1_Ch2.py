import turtle

#Write a program that displays the following information:
    #Your name
    #Your address, with city, state, and ZIP
    #Your telephone number
    #Your college major

# There are a few different ways to achieve this. The first method is below:
print("Name: Tyler Gates""\n""Address: 1600 Pennsylvania Avenue, Washington DC 20500""\n""Phone Number: (401)215-6334""\n""College Major: Cyber Security")
# The Second method is longer but allows for changes to be made on the fly without editing the print function:
name=input("Enter your First and last name:")
address=input("Enter your address:")
phone=input("Enter your Phone Number:")
major=input("Enter your Major:")
print(name, "\n", address, "\n", phone, "\n", major)

# A company has determined that its annual profit is typically 23 percent of total sales. Write
# a program that asks the user to enter the projected amount of total sales, then displays the
# profit that will be made from that amount.
# Hint: Use the value 0.23 to represent 23 percent.

projected=float(input("Enter the projected amount of total sales:"))
profit = projected * 0.23
print("Your profit will be ${:.2f}".format(profit))

# A customer in a store is purchasing five items. Write a program that asks for the price of
# each item, then displays the subtotal of the sale, the amount of sales tax, and the total.
# Assume the sales tax is 7 percent.

subtotal = 0

for item_num in range(1, 6):
    itm = float(input("Enter the grade for test number {}: ".format(item_num)))
    subtotal += itm
tax= float(subtotal)*0.07
finaltotal=float(subtotal)+float(tax)
print("Your subtotal is: $",subtotal, "\n" "Tax will be: $",tax, "\n" "Your total after tax is: $",finaltotal)


# Write a program that asks the user to enter the amount of a purchase and the desired
# number of payment instalments. The program should add 5 percent to the amount to get
# the total purchase amount, and then divide it by the desired number of instalments, then
# display messages telling the user the total amount of the purchase and how much each
# instalment will cost.

purchase_price=float(input("Enter the amount of a purchase:"))
num_payments=int(input("Enter the desired number of payments:"))
total_p= purchase_price+(purchase_price*0.05)
pmts= total_p/num_payments
print("The total purchase price is $",total_p, "and each payment in your",num_payments, "month long installment plan is $",pmts)


# Write a program that calculates the total amount of a meal purchased at a restaurant. The
# program should ask the user to enter the charge for the food, then calculate the amounts
# of a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

meal_base=float(input("Enter the charge for the food:"))
meal_tip=round(float(meal_base)*0.18,2)
meal_tax=round(float(meal_base)*0.07,2)
meal_total=round(meal_base+meal_tip+meal_tax,2)
print("You are paying $",meal_tax,"in taxes and you need to leave an 18% tip, which comes out to be $",meal_tip,"The total you should be paying for this meal is: $",meal_total)


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
s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("blue")
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
s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("blue")
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
s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("blue")
t.fillcolor("white")
t.begin_fill()
t.lt(90)
t.circle(60)
t.rt(90)
t.circle(-60)
t.penup()
t.goto(130,0)
t.pendown()
t.lt(90)
t.circle(60)
t.rt(90)
t.circle(-60)
t.penup()
t.goto(260,0)
t.pendown()
t.lt(90)
t.circle(60)
t.end_fill()
t.clear()


# Figure 5 (graph)
s = turtle.getscreen()
t = turtle.Turtle()
turtle.bgcolor("blue")
t.fillcolor("white")
t.begin_fill()
t.penup()
t.goto(0,-50)
t.pendown()
t.circle(50)
t.penup()
t.goto(0,0)
t.pendown()
t.fd(250)
t.penup()
t.goto(0,0)
t.pendown()
t.lt(90)
t.fd(250)
t.penup()
t.goto(0,0)
t.pendown()
t.lt(90)
t.fd(250)
t.penup()
t.goto(0,0)
t.pendown()
t.lt(90)
t.fd(250)
t.penup()
t.goto(0,0)
t.pendown()
t.end_fill()
t.clear()