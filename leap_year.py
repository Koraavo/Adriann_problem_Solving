print("Write a program that prints the next 20 leap years.")

is_leap = False
year = int(input("Enter the year "))
count = 0
list = []
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    is_leap = True
else:
    print("this is not a leap year")
    while is_leap == False:
        year += 1
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            is_leap = True


if is_leap == True:
    while count < 20:
        count += 1
        year +=4
        list.append(year)

    print("The next 20 leap years are ", list)