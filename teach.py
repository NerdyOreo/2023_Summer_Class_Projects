subtotal = 0

for item_num in range(1, 6):
    itm = float(input("Enter the grade for test number {}: ".format(item_num)))
    subtotal += itm
tax= float(subtotal)*0.07
finaltotal=float(subtotal)+float(tax)
print("Your subtotal is: $",subtotal, "\n" "Tax will be: $",tax, "\n" "Your total after tax is: $",finaltotal)