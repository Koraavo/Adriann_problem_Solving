print("2. Write a program that asks the user for a number n and" 
      "gives them the possibility to choose between computing the sum and computing the product of 1,…,n.")

def choices(number, choice):
    sum = 0
    multiply = 1
    if choice == "+":
        for i in range(1, number):
            sum = sum + i
        return "the sum of numbers from 1 to", number, "=", sum
    elif choice == "*":
        for i in range(1, number):
            multiply = multiply*i
        return "the multiplication of numbers from 1 to ", number, "=", multiply


print(choices(int(input("Enter the range: ")), input("Enter + or *: ")))