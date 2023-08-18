# Design a program that uses a loop to build a list named valid_numbers that contains only
# the numbers between 0 and 100 from the numbers list below. The program should then
# determine and display the total and average of the values in the valid_numbers list.
# numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

numbers = [74, 19, 105, 20, -2, 67, 7, 124, -45, 38]
total_num = 0
int_numbers = list(map(float, numbers))
valid_numbers = []
for picked_numbers in int_numbers:
    if 0 <= picked_numbers <=100:
        total_num += picked_numbers
        valid_numbers.append(picked_numbers)
    else:
        continue
total_val_num = len(valid_numbers)
average_num = total_num/total_val_num
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

