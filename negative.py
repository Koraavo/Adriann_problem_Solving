number = input("Enter your number: ")
if number.isalpha():
    print("This is not an integer")
elif number.startswith("-"):
    print(number[1:])
else:
    print(f"-{number}")

