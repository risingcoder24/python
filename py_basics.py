#print("Hello world")

# Drawing a shape

"""
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
"""

# Variables and data types

"""
character_name = "Cookie" #storing string
character_age =  "18"       #storing string

print("Hey I'm " + character_name +",")
print("I'm " + character_age +" years old")
print("I like singing")
"""

# Working with strings

"""
phrase="Walchand college"
#print(phrase + " is cool") #concatenation
print(phrase.lower())
print(phrase.upper())
print(phrase.islower())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[7])
print(phrase.index("Walch"))
print(phrase.replace("Walchand", "Cummins"))
"""

# Working with numbers

"""
from math import*    #math->module

print(2)
print(3*(4+5))
my_num=-5
print(my_num)
print(str(my_num) +" my fav number")
print(abs(my_num)) #gives the absolute value
print(pow(3,2))    #3 to the power 2
print(max(4,7))    #returns the highest value
print(min(4,7))
print(round(3.5))
print(round(3.2))
print(floor(3.7))  #this function will return the lowest value
print(ceil(3.7))   #this function will return the highest value
print(sqrt(64))
"""

# Getting input from the user

"""
name=input("Enter your name: ")
age=input("Enter your age: ")
print("Hello " + name + "! You are " + age)
"""

# Building a basic calculator

"""
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)
"""

# Mad libs game

"""
color=input("Enter a color:")
plural_noun=input("Enter a plural noun:")
celebrity=input("Enter a celebrity:")

print("Roses are " + color) 
print(plural_noun +" are blue")
print("I love " + celebrity)
"""

# Lists

"""
friends = ["Nikita", "Manasi", "Vidisha", "Arya"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])
friends[2]="Trupti"
print(friends[2])
"""

# List functions

"""
lucky_numbers = [4, 6, 8, 12, 16, 24]
friends = ["Nikita", "Manasi", "Vidisha", "Arya", "Manasi"]

friends.append("Sakshi")
#friends.extend(lucky_numbers) #adds two lists together
friends.insert(1,"Trupti")
friends.remove("Trupti")
#friends.clear()
friends.pop()

print(friends)

print(friends.index("Manasi"))
print(friends.count("Manasi"))

friends.sort()
print(friends)

lucky_numbers.sort
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2=friends.copy()
print(friends2)
"""

# Tuples --> cannot be modified

"""
coordinates =[ (4, 5), (6,6), (9,0) ]

print(coordinates[2])
"""

# Functions

"""
def say_hi(name,age):
    print("Hello " + name + ", You're " + str(age))
    
say_hi("Khushi", 19)
say_hi("Manasi", 20)
"""

# Return statement

"""
def cube(num):
    return num*num*num

result = cube(4)
print(cube(3))  
print(result)  
"""

# If statements

""""
is_female = False
is_tall = False

if is_female or is_tall:  #"and" is aslo a keyword 
    print("You are a female or tall or both")
elif is_female and not (is_tall):
    print("You are a short Female")
elif not(is_female) and is_tall:
    print("You are not a Female but are short")
else:
    print("You are not a female nor tall")
"""

# If statements and comparision

"""
def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        print(num1)
    elif num2>=num1 and num2>=num3:
        print(num2)
    else:
        print(num3)

def string_comp():
    if "dog"=="doog":
        print("Equal")
    else:
        print("Not equal")
        
max_num(4,8,2)
string_comp()
"""

# Building a better calculator

"""
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1/num2)
elif op == "*":
    print(num1*num2)
else:
    print("Invalid Operator")
"""

# Dictonaries

"""
monthConversions = {
    "Jan":"January", #keys can be numbers
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
    }

#print(monthConversions["Aug"])
print(monthConversions.get("Dec"))
print(monthConversions.get("luv", "Not a valid key"))
"""

# While loop

"""
i = 1
while i <= 10:
    print(i)
    i += 1
"""

# Building a guessing game

"""
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")
"""

#For loop


