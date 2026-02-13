#1.Comparison and Conditionals

##Exercise 1: Comparison Operators
x = 5
y = 4
is_true = x > y
print(is_true)

x = 4
y = 5
is_false = x > y
print(is_false)

x = 4
y = 5 
is_true = x < y
print(is_true)

x = 5
y = 4 
is_false = x < y
print(is_false)

x = 5
y = 4 
is_false = x != y
print(is_false)

##Exercise 2: Logical Operators

age = 25
is_in_age_range = age > 20 and age < 30
print(is_in_age_range)

age = 25
is_in_age_range = age > 20 and age > 30
print(is_in_age_range)

age = 25
is_in_age_range = age > 20 or age > 30
print(not (is_in_age_range))

age = 25
is_in_age_range = age > 20 or age > 30
print(is_in_age_range)

age = 25
is_in_age_range = age > 20 and age < 30
print(not(is_in_age_range))

##Exercise 3: if – Conditionals

age = 19
age_group = "child"

if age > 18:
    age_group = "adult"

print(f"The age group is {age_group}")


age = 14
age_group = "child"

if age > 18:
    age_group = "adult"

print(f"The age group is {age_group}")


##Exercise 4: if – else Conditionals

wind_speed = 30

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")


wind_speed = 8

if wind_speed < 10:
    print("It is a calm day")
else:
    print("It is a windy day")


##Exercise 5: if – elif - else Conditionals

grade = 80

if grade < 50: 
    print("You failed") 
elif grade < 60: 
    print("You passed") 
elif grade < 70: 
    print("You got a good pass")
else:
    print("You got an excellent pass")

##Exercise 6: Summary Tasks

temperature1 = 20
temperature2 = 40
 
if temperature1 == temperature2:
    print("The temperature is the same")
else:
    print("The temperature is different")

temperature1 = 20
temperature2 = 20

if temperature1 == temperature2:
    print("The temperature is the same")
else:
    print("The temperature is different")

#2. Python Lists

##Exercise 1: Creating a list

integer_list = [1, 2, 3, 4, 5] 
string_list = ["apple", "banana", "orange", "grape"] 
empty_list = [] 
list_with_different_types = [1, "two", 3.0, True] 

person_1_age = 20 
person_2_age = 30 

# creating a list based on variables 
age_list = [person_1_age, person_2_age]

list_within_a_list = [["red", "green", "blue"], ["yellow", "orange", "purple"]]

###Task = Create a list in the variable city_list.
city_list = ["Glasgow", "London", "Edinburgh"]
print(city_list)

##Exercise 2: Accessing a list

second_item = string_list[1]
print(second_item)

slicing_item = string_list[0:2]
print(slicing_item)

last_item = string_list[-1]
print(last_item)

###Task: Print the third item in the city_list list. Then print the last two items in the city_list list as well using slicing

third_item = city_list[2]
print(third_item)

slicing_last_two_item = city_list[1:3]
print(slicing_last_two_item)

###Modifying a list

string_list[0] = "pear"
print(string_list)

string_list.append("orange")
print(string_list)

### Task: Add the item "Manchester" to the end of the city_list list. Then change the second item in the city_list list to "Birmingham".
city_list.append("Manchester")
print(city_list)

city_list[1] = "Birmingham"
print(city_list)

##Exercise 4: Summary Task

colours = ["red", "yellow", "green"]
print(colours)

second_element = colours[1]
print(second_element)

colours[0] = "black"
print(colours)

list_length = len(colours)
print(list_length)

if "red" in colours:
    print("Red is in the list")
else:
    print("Red is not in the list")

selected_colours = colours[1:3]
print(selected_colours)

## 3. Python Loops

### Exercise 1: While Loops

i = 0 
while i < 5: 
    print(i) 
    i += 1

### Exercise 2: For Loops

string_list = ["apple", "banana", "orange", "grape"]
for fruit in string_list: 
    print(fruit)

### Task: Create a for loop that prints each item in the city_list list.

city_list = ["Glasgow", "London", "Edinburgh"]   
for city in city_list: 
    print(city)

### Exercise 3: Loop Keywords: Range, break and continue
range(0, 5) # will return [0, 1, 2, 3, 4] 
range(5) # will return [0, 1, 2, 3, 4] 
range(0, 5, 2) # will return [0, 2, 4] because the third parameter is the step size 
range(5, 0, -1) # will return [5, 4, 3, 2, 1]

for i in range(5): 
    print(i)

for i in range(5): 
    if i == 2: 
        break 
    print(i)

### Task: Modify the above code to print the numbers 0 through 4, but stop the loop when i is equal to 3.
for i in range(5): 
    if i == 3: 
        break 
    print(i)

for i in range(5): 
    if i == 2: 
        continue 
    print(i)

#### Exercise 4: Summary Tasks

### Task – Even Numbers
numbers = list(range(1,11))
print(numbers)

for i in numbers:
    if i % 2 == 0:
        print(i)

### Task – Sum of Squares
sum_of_squares = 0

for i in range (1,6):
    sum_of_squares += i ** 2 

print(sum_of_squares)

### Task – Countdown:
countdown = 10

while countdown >= 1:
    print(countdown)
    countdown -= 1
print("Liftoff!")

#### 4. Obtaining User Input
### Example: Entering a basic string

user_input = input("Enter something: ") 
print("You entered:", user_input)

### Example: Entering a number
age = input("How old are you? ") 

# Convert the age to an integer 
age = int(age) 

next_year_age = age + 1 
print("Next year, you'll be", next_year_age, "years old.")

### Task: User Input and Conditional Statements
user_age = input("How old are you? ")
user_age = int(age)

if user_age < 18:
    print("You are a minor")
elif 18 <= user_age <= 65:
    print("You are an adult.")
else: user_age > 65
print("You are a senior citizen.")

### Task: Temperature Converter
# Welcome message
print("Welcome to the Temperature Converter!")

# User input for Celsius temperature
celsius_input = float(input("Enter the temperature in Celsius: "))

# Convert Celsius to Fahrenheit
degree_f = (celsius_input * 9/5) + 32

# Convert Celsius to Kelvin
degree_k = celsius_input + 273.15

# Results Output
print(f"\nThe temperature you have entered is {celsius_input}°C.")
print("Converted Temperatures:")
print(f"{celsius_input}°C is equal to {degree_f:.2f}°F.")
print(f"{celsius_input}°C is equal to {degree_k:.2f} K.")
print("Thank you for using the Temperature Converter!")

#### Extra task
# Welcome message
print("Welcome to the Temperature Converter!")

# Ask for temperature scale
scale = input("Enter the scale of the temperature you have (C, F, or K): ").upper()

# Get temperature value
temp = float(input(f"Enter the temperature in {scale}: "))

# Perform conversions based on input scale
if scale == "C":
    f = (temp * 9/5) + 32
    k = temp + 273.15
    print(f"\n{temp}°C is equal to {f:.2f}°F and {k:.2f} K.")

elif scale == "F":
    c = (temp - 32) * 5/9
    k = c + 273.15
    print(f"\n{temp}°F is equal to {c:.2f}°C and {k:.2f} K.")

elif scale == "K":
    c = temp - 273.15
    f = (c * 9/5) + 32
    print(f"\n{temp} K is equal to {c:.2f}°C and {f:.2f}°F.")

else:
    print("Invalid input. Please enter C, F, or K.")

print("Thank you for using the Temperature Converter!")

