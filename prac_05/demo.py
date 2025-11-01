name_to_age = {"Bill": 17, "Jane": 34, "Jack": 56,
"Sven": 13}
result = {name: age for name,
age in name_to_age.items() if age < 18}
print(result)

name_to_age[input("Name: ")] = int(input("Age: "))
print(name_to_age)

#
my_subjects = {'CP1401', 'CP1404', 'MA1000'}
your_subjects = {'CP1404', 'MA1008', 'NM1010'}
print("union: ", my_subjects | your_subjects)
print("difference: ", my_subjects - your_subjects)
print("intersection: ", my_subjects & your_subjects)
print("symmetric difference: ", my_subjects ^
your_subjects)





# name = input("Name: ")
# age = int(input("Age: "))