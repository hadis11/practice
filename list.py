# a shopping List
shopping_list = ["milk", "eggs", "bread", "cheese", "apples"]
# Indexing
print(shopping_list[-1])
print(shopping_list[3])
# slicing
print(shopping_list[::2])
print(shopping_list[:2:-1])
# for loop with list
for item in shopping_list:
    print(f" dont  forget to buy {item}!")

# SHOPPING CARTS
shopping_cart = ["apple", "banana", "milk", "eggs", "bread"]
prices = [1.25, 0.75, 3.50, 2.25, 2.75]
# calculate the total cost
total_cost = 0 
for i in range (len(shopping_cart)):
    total_cost += prices[i]
print(f"  total cost is : {total_cost}")
# Remove an item from the cart
shopping_cart.remove("milk")
print(f"updated shopping cart: {shopping_cart}")
# Add a new item to the cart
shopping_cart.append("cheese")
print(f"updated shopping cart:{shopping_cart}")

# MOVIE RATINGS
movie_rating = [4.5, 3.8, 5.0, 2.5, 4.2, 3.0]
# find the average rating
total_rating = 0
for rating in movie_rating:
    total_rating += rating
average_rating = total_rating / len(movie_rating)
print(f"average rating is: {average_rating}")
# get the highest_rated movie
highest_rating = max (movie_rating)
print(f"The highest_rated movie is:  {highest_rating}")
# print all ratings above 4.0
for rating in movie_rating:
    if rating > 4.0:
        print(f"rating above 4.0 for this movie is:{rating}")

# STUDENT GRADES
student_grades = {"Alice":85, "Bob":92, "Charlie":78, "Diana":95}
# find the student with the lowest grade
worst_grade = 78
worst_student = ""
for student, grade in student_grades.items():
    if grade < worst_grade:
     worst_student = student
    worst_grade = grade
print(f"the worst student is {worst_student} with grade {worst_grade}")

# use range ()to iterate over a list using for loops   range(start, stop(not included), step)
my_list = [ "milk", "eggs", "bread", "cheese", [11, "salad"],  "apples" ]
for i in range (0, len(my_list), 2 ):
    print(my_list[i])
# print the first 3 elements
for i in range(3):
    print(my_list[i])
# print the elements from index 2 to the end
for i in range (2,len(my_list)):
    print(my_list[i])

# methods that can be applied to the list

#append(x)
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

#clear()
my_list =[1, 2, 3]
my_list.clear()
print(my_list)
