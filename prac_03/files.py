"""
CP1404/CP5632 - Practical
Do-from-scratch Exercises
"""

#1
name = input("Name: ")
out_file = open("name.txt","w")
out_file.write(name)
out_file.close()



#2
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(name)



#3
with open("numbers.txt", "r") as in_file:
    first_number = in_file.readline()
    second_number = in_file.readline()
result = int(first_number) + int(second_number)
print(result)



#4
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)