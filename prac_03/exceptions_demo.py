"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Can not divide by zero!!! Please enter another number")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
        print("Numerator and denominator must be valid numbers!")
print("Finished.")

#1  When one enters something that is not a valid integer.
#2  When one enters 0 for the denominator.