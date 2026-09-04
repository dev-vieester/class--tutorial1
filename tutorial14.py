# def convert_to_lowercase(value:str, database: list[str]) -> list[str]:
#     data = value.lower()
#     db = database.append(data)
#     return db
# #DRY (Do not repeat yourself)
# user_email = []
# user_name = []
#
# email = input("Please enter you name: ")
# convert_to_lowercase(email, user_email)
# # value = email.lower() #Convert to lower case
# # user_email.append(value) #save in our database
#
# username = input("Please enter your user name: ")
# convert_to_lowercase(username, user_name)
# # value = username.lower() #Convert to lowercase
# # user_name.append(value) #save in our database

#To create a function you start with the def key word, then give your function a descriptive name follow by open and close bracket
#then a colum, follow by the task body.
# def addition():
#     print(2 + 2)
#
# addition()


#parameter and argument(They are both input that we give out function), note a function can take parameter
# or be without parameter
# def morning_greetings(name):
#     print(f"Good morning {name}")
#     print("ensure you eat you break fast")
#     print("also go out with umbrella incase it rain")
#
# def afternoon_greetings(name):
#     print(f"Good afternoon {name}")
#     print("Ensure you eat you launch")
#     print("dont forget to complete you office task")
#
# def night_greetings(name):
#     print(f"Good Night {name}")
#     print("Ensure to off the light before sleeping")
#
#
# value = "Night"
#
# if value == "Morning":
#     morning_greetings("Jennifer")
# elif value == "Afternoon":
#     afternoon_greetings("Jennifer")
# else:
#     night_greetings("Jennifer")

# def simple_calculator(num1:int, num2:int, operator:str):
#     result = 0
#     if operator == "+":
#         result = num1 + num2
#     if operator == "-":
#         result = num1 - num2
#     print(result)
#
# simple_calculator(60, 4, "+")
# simple_calculator(8, 3, "-")

#return
# def simple_calculator(num1:int, num2:int, operator:str):
#     result = 0
#     if operator == "+":
#         result = num1 + num2
#     if operator == "-":
#         result = num1 - num2
#     return result #64
#
# new_value = simple_calculator(60, 4, "+")
# print(new_value)
# new_value_2 =simple_calculator(8, 3, "-")
# print(new_value_2)

def convert_naira_to_dollar(naira_value: float) -> str:
    one_naira = 1400.00
    convert_to_dollar = naira_value/one_naira
    return f"{convert_to_dollar:.2f}"

def calculate(): #Creating an empty function
    pass

value = convert_naira_to_dollar(10000)
# print(value)

#Positional parameter
#named parameter
#default parameter

def show_data(name:str, age:int, complexion = "Light"):
    print(f"Hello {name} your age is {age} and you will {age + 10} in 2032 "
          f"and you complexion is {complexion}")

show_data(age=10, name="Awele", complexion="Dark") #Named parameter
# show_data(20, "Jennifer") #Positional parameter - i will get error because of position













