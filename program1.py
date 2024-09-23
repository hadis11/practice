# Sum of Numbers: Write a program that calculates the sum of all integers from 1 to 100 using a for loop.
total=0
for number in range(1,101):
#gpt
    total +=number 
print(total)   
# Factorial Calculation: Write a program that computes the factorial of a number (e.g., 5!) using a while loop.
import math
n=0
factorial = 1
while n<5:
    n +=1
    factorial *=n
    print(factorial)
# Even Numbers: Write a program that prints all odd numbers between 1 and 50 using a for loop and an if statement.
for i in range(1,51):
    if i%2 !=0 :
        print(f"odd number: {i}")
# Multiples of 3 0r 5: Write a program that prints numbers between 1 and 100 that are divisible by 3 or 5 using a for loop and if statements.
for i in range(1,101):
    if i%3 == 0 :
        print("divisible by 3 : ", i)
    elif i%5 == 0:
        print("divisible by 5 : ", i)
# Sum of List Elements: Write a program that sums up all the elements in a given list [1, 2, 3, 4, 5] using a for loop.
#gpt
numbers = [1, 2, 3, 4, 5]
total =0
for i in numbers:
    total+= i
print("total numbers:" , total)
# List of Squares: Write a program that creates a list of the squares of numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i**2,end=" , ")
print()
for i in range(1,11):
    if i**2 < 10:
        print(i)
print("****")
# Find Maximum in List: Write a program that finds the maximum number in a given list [3, 5, 7, 2, 8].
numbers = [3, 5, 7, 2, 8]
max_number = max(numbers)
print("The maximum number is:", max_number)
string = ["pharmasist", "hadis", "Do it,you can", "I Love You"]
max_string = max(string, key=len)
print("do The largest string is: " , max_string)

# while loop practice
# Print numbers 1 to 10 but stop the loop when the number reaches 7
count = 0
while count < 7 :
    count+=1
    print(count)
    if count == 6 :
        break
#gpt
i = 1
while i <= 10 :
    if i == 7:
        break
    print(i)
    i+=1
# Print all even numbers between 1 and 10 but skip the number 6
i = 0 
while i <=8 and i % 2 ==0 :
    i+=2
    if i ==6 :
        continue
    print (i)
#gpt
i = 1
while i <= 10 :
    i+=1
    if i == 6:
        continue
    elif i % 2 ==0 :
        print(i)
# separate even & odd number from the list
a = [1, 2, 3, 4, 5, 10, 7, 9, 8]
b= []
c= []
for i in a:
    if i %2 ==0:
        b.append (i)
        b.sort()
        # b += [i]
    else:
        c.append(i)
        c.sort()
        # c += [i]
print("even numbers list:", b)
print("odd numbers list:", c)

        


