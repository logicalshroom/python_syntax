# Objective 3 Task 1 : Grocery Store Math

# Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices.

bread, milk, eggs = 7.99, 4.99, 37.99 # Make up some values of grocery store items, assign their costs

print(f"The cost of your grocery store bill is ${bread+milk+eggs}!") # Print a string that adds together all the variables

# Objective 3 Task 2 : Bank Interest

# You have a savings account with a particular initial amount, and a fixed yearly interest rate. Calculate the total amount in your account after 1 year.

deposit = 10000 # Assign initial deposit variable

interest_rate = .07 # Assign interest rate, we will just make it a float to make life easy

total_amount = deposit+(deposit*interest_rate) # And then we do our math math. We add the initial deposit to the interest, and assign a new variable

print(f"Your total amount after one year of interest is: ${int(total_amount)}!") #I want it to print as a speciifc dollar amount so we are gonna force it to output an integer



