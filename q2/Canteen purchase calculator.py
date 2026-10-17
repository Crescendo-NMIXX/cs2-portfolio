#This calculates and returns the total purchase cost by multiplying the price of an item by the quantity purchased.
def calculate_total(price, quantity):
  return price * quantity
  
# This function calculates the customer's change.
#If the customer does not pay enough, it calculates how much more money is needed instead of showing a negative change.
def calculate_change(payment, total):
    if payment >= total:
        return payment - total
    else:
        return total - payment

#This asks for the price, value, and amount paid
item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
payment = float(input("Enter amount paid: "))

total_cost = calculate_total(item_price, quantity)

change = calculate_change(payment, total_cost)

#This displays the results 
print(f"Total Cost: PHP {total_cost:.2f}")

if payment >= total_cost:
    print(f"Change: PHP {change:.2f}")
else:
    print(f"Additional amount needed: PHP {change:.2f}")

#1. What does each function do?

#The calculate_total() function gets the total cost by multiplying the price by the quantity. The calculate_change() function calculates how much change the customer will get or how much more money they need to pay.

#2. What is the difference between the parameters price and quantity and the actual arguments passed to the function?

#Parameters are the names used inside the function, like price and quantity. Actual arguments are the values we give to the function when we call it, like the item's price and the number of items bought.

#3. Where is the returned total stored, and how is it reused?

#The total cost is stored in the variable total_cost. The program then uses it in the calculate_change() function to find out how much change the customer gets or how much more they need to pay.

#4. Why is it useful to separate total calculation from change calculation?

#It is useful because the program becomes easier to understand and fix if there are mistakes. Each function has its own job, so the code is more organized and can be reused in other programs.
