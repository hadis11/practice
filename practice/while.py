a = "1234"
string_length = len(a)
print(string_length)
my_list = [1, 2, 3, 4, 5]
list_length = len(my_list)
print(list_length)
my_tuple = (1, 2, "apple", "banana")
tuple_length = len(my_tuple)
#1
a = 1458746
counter = 0
while a != 0 :
    a= a//10
    counter +=1
    print(counter)
print("........")

count = 5           
while count > 0 :
    count -= 1
    if count == 2:
        continue
    print(count)
print(".........")

count = 5
while count > 0 :
    print(count)
    count -=1
    if count == 3:
        break 
print("Exited the loop")


count = 5
while count > 0 :
    count -= 1
    if count == 2:
        continue
    print(count)
print("........")

a = "1234"
length_number = len(a)
print(length_number)

a = 1234
counter = 0
while a!= 0 :
    a= a // 10
    counter +=1
    print(counter)
print("....")
a = 103345344323554234
counter = 1
while a >= 10:
    a = a //10
    counter +=1
print(counter)

# input
s = "12 C C VFB DB!! asrgkecps"
upper_counter = 0
lower_counter = 0
non_letter_counter = 0
for i in s:
    if i.isupper():
        upper_counter +=1
    elif i.islower():
        lower_counter +=1
    else:
        non_letter_counter +=1
       
print("number of upper letters:", upper_counter)
print("number of lower counter:", lower_counter)
print("number of non letter counter:", non_letter_counter)

# import
import random
print(random.randint(10,20))
import math
result = math.sqrt (16)
print(result)
# find the sine of 30 degrees
angle_in_radians = math.radians(30)
sine_value = math.sin(angle_in_radians)
print(sine_value)

# import specific Items
from math import sqrt 
result = sqrt(64)
print(result)
from math import *
result = sin(45)
print(result)

# dot (.) operator
my_list = [1, 2, 3]
print(my_list.append(4))
print(my_list)
class Dog :
    def bark(self):
        print("Woof!")
my_dog = Dog()
my_dog.bark()
my_dict ={"name": "Bob", "age" : 24}
print(my_dict["name"])
name = "hadis"
age = 24
message = "My name is {} and I am {} years old.".format(name, age) 
print(message)
my_string = "hello world".upper()
print(my_string)

#input function
name = input("what is your name? ")
print("Hello," , name)
#getting a number
age = input("Enter your age: ")
age = int(age) #covert the input string to an integer
print("You are", age , "years old.")
# basic calculator
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the scond number:"))
sum = num1 + num2
print("The sum is:", sum)