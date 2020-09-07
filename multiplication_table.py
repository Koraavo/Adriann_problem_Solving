print("3. Write a program that prints a multiplication table for numbers up to 12.")


for i in range(1, 13):
    for j in range(1, 13):
        tables = j*i
        print(i, "x", j, "=", tables)


print("or")
i = 0
while i < 13:
    i += 1
    for x in range(1, 13):
        mul = x*i
        print(i, "x", x, "is", mul)

