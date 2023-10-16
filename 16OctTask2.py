# Create a program that determines whether a given year is a leap year.
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
# Use an if-else statement to make this determination.
#
# Input = 2024
# Output = Leap year

year=int(input("Enter the Year"))
if year / 100 != 400:
    print("Leap Year")
else:
    print("Not Leap Year")