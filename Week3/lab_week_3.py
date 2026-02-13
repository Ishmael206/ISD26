#1.Functions and Scope
##Exercise 1: Functions in Python

###Creating Functions

def greet_user():
    print("Hello!")
greet_user()

###Function Parameters

def greet_user(name):
    print(f"Hello{name}!")
greet_user("Thomas")

def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
greet_user("Thomas","Musah")

###Keyword Arguments

def greet_user(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")
greet_user(last_name ="Musah",first_name ="Thomas")

###Default Values

def greet_user(first_name, last_name, university="UWS"):
    print(f"Hello {first_name} {last_name} from {university}!")
greet_user("Thomas","Musah")

def greet_user(first_name, last_name, university="UWS"):
    print(f"Hello {first_name} {last_name} from {university}!")
greet_user("Thomas","Musah","UWS Paisley")

###Task: Create a function called greet_friends.

def greet_friends(names):
    for name in names:
        print(f"Hello {name}!")

friend_list = ["John", "Jane", "Jack"]
greet_friends(friend_list)

###Return

def add_number(num1,num2):
    return num1 + num2

result = add_number(5,10)
print(result)

def add_numbers(num1, num2):
    result = num1 + num2

    return result

result = add_numbers(5, 10)
print(result)

def add_and_multiply_numbers(num1, num2):
    return num1 + num2, num1 * num2

result = add_and_multiply_numbers(5, 10)
print(result)

def add_and_multiply_numbers(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    return sum, product

sum, product = add_and_multiply_numbers(5, 10)
print(sum)
print(product)

#Task Tax Calculation: 
def calculate_tax(income, tax_rate):
    income_tax = income * tax_rate
    return income_tax

income = 50000
tax_rate = 0.2

calculate_tax = calculate_tax(income, tax_rate)
print(f"The calculated Tax is £{calculate_tax}")

#Using different income and tax rate
def calculate_tax(income, tax_rate):
    income_tax = income * tax_rate
    return income_tax

income = 100000
tax_rate = 0.5

calculate_tax = calculate_tax(income, tax_rate)
print(f"The calculated Tax is £{calculate_tax}")

#Task Compound Interest Calculator Function
def compound_interest(principal, duration, interest_rate):
     
     # Validate the interest rate
    if interest_rate < 0 or interest_rate > 1:
        print("Please enter a decimal number between 0 and 1")
        return None
    
    # Validate the duration
    if duration < 0:
        print("Please enter a positive number of years")
        return None
    
    # Calculate and print the investment amount for each year
    for year in range(1, duration + 1):
        total_for_the_year = principal * (1 + interest_rate) ** year
        print(f"The total amount of money earned by the investment in year {year} is {total_for_the_year:.2f} £")

    # Return the final investment value as an integer
    final_amount = principal * (1 + interest_rate) ** duration
    return int(final_amount)

# Test the function
result = compound_interest(1000, 5, 0.03)
print(f"Final investment value after 5 years: £{result}")

##Exercise 2: Variable Scope
"""
def new_function():
    my_new_variable = 5

new_function() # call the function. No problems here.

print(my_new_variable) # this will cause an error
"""
my_new_variable = 0

def new_function():
    my_new_variable = 5

new_function()

print(my_new_variable)

#2.Optional: Assertions and Errors
##Exercise 6: Assertions
assert compound_interest(1000, 5, 0.03) == 1159

##Exercise 7: Identifying and Fixing Common Errors
"""
print("Hello World!) #Syntax Error

my_name = "Alice"
print("Hello, " + myname) #Name Error

my_string = "Hello World"
print(int(my_string)) #Value Error

fruits = ["apple", "banana", "orange"]
print(fruits[3]) #Index Error

if 5 > 2:
print("Five is greater than two!") #Indentation Error
"""

#Task - Fixing Errors:
##Syntax Error
""""
pritn("Hello, World!")
"""
print("Hello World!")

##Name Error
""""
print("My favorite color is", favorite_color)
"""
favorite_color = "Blue"
print("My favorite color is", favorite_color)

##Value Error
""""
number1 = "5"
number2 = 3
result = number1 + number2
print("The sum is:", result)
"""

number1 = 5
number2 = 3
result = number1 + number2
print("The sum is:", result)

##Index Error
"""
fruits = ["apple", "banana", "cherry"]
print(fruits[3])
"""

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

##Indentation Error
"""
time = 11
if time < 12:
print("Good morning!")
"""

time = 11
if time < 12:
    print("Good morning!")

#3. Your first larger-scale Python programme 