print("4. Write a program that prints all prime numbers. "
      "(Note: if your programming language does not support arbitrary size numbers, "
      "printing all primes up to the largest number you can easily represent is fine too.)")

# list = [2]
#
# for i in range(3, 10000, 2):
#     prime = True
#     for j in range(2, i):
#         if (i%j == 0):
#             prime = False
#     if prime:
#         list.append(i)
# print(list)

prime_numbers = [n for n in range(2, 1000) if all(n % x for x in range(2, n))]
print(prime_numbers)
for n in range(2, 1000):
    if all(n%x for x in range(2, n)):
        print(n)
