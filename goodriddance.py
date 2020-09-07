"""
After gathering the four names, ages and shoe sizes,
ask the user to enter the name of the person they want to remove from the list.
Delete this row from the data and display the other rows on separate lines.
"""
list = {}
for i in range(4):
    name = input("NAME: ")
    age = input("Age: ")
    shoe = input("Shoe: ")
    list[name] = {"Age": age, "Shoe": shoe}

getrid = input("who do you want to get rid of? ")
del list[getrid]

for i in list:
    print(i, list[i]['Age'], list[i]['Shoe'])