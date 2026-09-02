#Condition statement
#if (condition):
    #result
# value = 12
# age = 20
# if value > 12:
#     print(f"{value} is greater than 12")
# elif value < 12:
#     print(f"{value} is less than 12")
# elif value == 12:
#     print(f"{value} is equal to 12")
# else:
#     print("No value to compare with")
#
# print("Hello")
from tutorial3 import is_boy

# age = 20
# gender = "Allein"
#
# if gender == "Male":
#     if age > 18:
#         print("You have mustache")
#     else:
#         print("You dont have mustache")
# elif gender == "Female":
#     if age > 18:
#         print("You are an adult")
#     else:
#         print("You are not an adult")
# else:
#     print("You are not a human being")
#0 - False 1 - True "" -False None
# value = "Awele"
#
# if value:
#     print("hello")
# else:
#     print('No greeting')

#Single line condition
# gender = "Girl"

# if gender == "Boy":
#     print("wash car")
# else:
#     print("Cook food")

# game = "wash car" if gender == "Boy" else "Cook"
# print(game)

# a = 5
# b = 2
# if a > b: print("a is greater than b") #Use for just single condition check
#
#
# #Short Hand If ... Else
# a = 2
# b = 330
# print("A") if a > b else print("B") #Result when it's true by the left hand, condition in the middle, and result when it's false by the right hand

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")

#Comparing multiple condition statement using (and, or ,not)
#for (and) Condition A must be true and Condition B must also be True - True
#for (Or) One of the conditions must be true - True
# temperature = 25
# is_raining = False
# is_weekend = True
#
# if (temperature > 20 and not is_raining) or is_weekend:
#     print("Great day for outdoor activities!")

# username = "Tobias"
# password = "secret123"
# is_verified = True
#
# if username and password and is_verified:
#   print("Login successful")
# else:
#   print("Login failed")

#Match or Switch Statement
day_of_the_week = "Tuesday"

match day_of_the_week:
    case "Monday":
        print("We are going to work")
    case "Tuesday":
        print("We are going to work and church")
    case "Wednesday":
        print("We are going to work and market")
    case _:#else
        print("No work")




