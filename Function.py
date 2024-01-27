# Create and Call
# def greet():
#     print("Hello Stranger!")
#     print("Nice to meet you")
# greet()

##################################################################################################

# Passing Arguments
# def greet(name):
#     print("Hello, " + name)

# greet("Amanda")
# greet("Durjanah")
# greet("Munah")

# def greet(name, age):
#     print("Name :  " + name)
#     print("Age : " + str(age))
# greet("Amanda", 20)
# greet(age = 20, name = "Amanda")

##################################################################################################

# Lambda Function
# def add5(x):
#     return x + 5
# print(add5(2)) # 7

# add5 = lambda x: x + 2
# print(add5(2)) # 4

# def add5(numbers):
#     total = number + 5
#     return total

# number = 10
# number_added_5 = add5(number)
# print(number_added_5)

number = 10
total = lambda n: n + 5
print(total(number))