# 1, 2, 3
# 10, 20, 30, 40, 50, 60
for i in range(1, 3 + 1):
    for j in range(10, 60 + 1, 10):
        print(i, ":", j)
# python for Loop with Tuples
numbers = (34, 54, 67, 21, 78, 97, 45, 44, 80, 19)
total = 0
for num in numbers:
    total += num
    print("total =", total)
# python for Loop with Lists
numbers = [34, 54, 67, 21, 78, 97, 45, 44, 80, 19]
total = 0
for num in numbers:
    if num % 2 == 0:
        print(num)
# use of range with for loop
# range(start,stop,step):
for num in range(5):
    print(num, end='   ')
print()
for num in range(10, 20):
    print(num, end='  ')
print()
for num in range(1, 10, 2):
    print(num, end='')
    print()
# Generating  a 3D pattern
for layer in range(4):
    print(f"layer {layer + 1}:")
    for row in range(4):
        for column in range(4):
            for depth in range(4):
                if depth == layer:
                    print("*", end=' ')
                else:
                    print(" ", end=" ")
                print("", end="")
            print()
        print("^" * 20)
# Generating a 3D pattern
for layer in range(4):
    for row in range(4):
        for column in range(4):
            for depth in range(4):
                if (depth == layer) and (column == row):
                    print("*", end="")
                else:
                    print(" ", end="")
        print(" ", end="")
        print()
    print("-" * 20)
# Loop with Dictionaries
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
for x in numbers:
    print(x, ":", numbers[x])
# the dict-items object
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
for x in numbers.items():
    print(x)
