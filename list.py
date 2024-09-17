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
