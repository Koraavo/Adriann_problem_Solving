import random

name = input("Enter your name ")
print("hallo", name, "guess my number chosen between 1 and 20")
print("you have a total of four guesses")
secret_number = random.randrange(1, 21)
count = 0
list_of_guesses = []

while count < 4:
    user_number = int(input("Make a guess: "))
    count += 1
    if user_number in list_of_guesses:
        print("you have already given that number")
        count -= 1

    if user_number + 2 == secret_number or user_number - 2 == secret_number:
        print("you are close to the secret number")
        list_of_guesses.append(user_number)
    if user_number + 1 == secret_number or user_number - 1 == secret_number:
        print("you are very close to the secret number")
        list_of_guesses.append(user_number)
    elif user_number < secret_number:
        print("the number is lower than the secret_number")
        list_of_guesses.append(user_number)
    elif user_number > secret_number:
        print("the number is higher than the secret number")
        list_of_guesses.append(user_number)
    elif user_number == secret_number:
        break

if user_number == secret_number:
    print("YAY, you got the number in", count, "guesses")

if user_number != secret_number:
    print("Sorry, the number I was thinking of was ", secret_number)


