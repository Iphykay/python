sentence = f'The Labwork \tWork'
print(sentence)

# \r moves the cursor to the begining of the line(after the nextline) and then keeps outputting 
# characters as normal. Which is ESCAPE.

# ith row is the vertical one and jth column is the horizontal one
# Reverse a list using an index slicing operation r[::-1]



print("Welcome to the", end=" ")
print("PHD Program in", end=" ")
print("Imaging Science")

print('G','F', sep='', end=" ")
print('G')

vars()

dir() # function that returns all properties and methods of the specified object without values. 

globals() # returns the name, properties and methods

# import getpass
# password = getpass.getpass('Password: ')   #The create password inputs

comedian = {'name': 'Iphy Kelvin', 'age': 29}
r = f"I am {comedian['name']} and I am {comedian['age']} years old"
print(r)

#To get the size of the memory of a saved variable
from sys import getsizeof

var = "Hello"
print(getsizeof(var), "[bytes]")

var1 = f"Hello"
print(getsizeof(var), "[bytes]")

#Convert integer number into binary
bin1 = bin(10)
print(bin1)

#Sets: A collection which is unordered, unchangeable and unindexed. No duplicate members
var_set = set(['a', 'PythoN', 1, 2, 1, 2, 3.14159, 121, 0b11, 0o11, 0x11, 2+3j])
print(var_set)

#Frozen Sets: Cannot be changed once created.
normal_set = set(["E1","E2","E3"])
normal_set.add("NEW ELEMENT")

Frozen_set = frozenset(["fE1","fE2","fE3"])
print(Frozen_set)

# Object Memory ID Based Conditions
var2 = 2
id(var2)

# Recursive Statement
# When an algorithm is using the revious output to calculate the 
# current/future outputs
# Eg Recursive Factorial Sequences
def Recursive_Factorial(n):
    if n == 1:
        return n
    else: 
        return n * Recursive_Factorial(n-1)


# Generator Function
# Written like a regular expression, therefore uses yield keyword
# It reduces memory

# words_list = ["night", "fifty", "maintain", "security", "state", "needle",
# "knowledge", "internal", "self", "shadow"]

# def contains_character(words, character):
#     for word in words:
#         if character in word:
#             yield word


# word_s = contains_character(words_list, "a")
# for word in word_s:
#     print(word)

# We can use next to output the elements in a generator
# Runtime
# Use import cProfile as profile
# print("Runtime for List Comprehension   :")
# profile_01 = profile.run("max([n**2 for n in range(1, 100000)])")
# print(profile_01)

# Decorators
# Takes another function as an argument, extending the behaviour of that function
# without explictly modifying that function. Closure is what the decorator outputs
# Eg
# def calculate():
#     num = 1
#     def inner_func():
#         nonlocal num
#         num += 2
#         return num
#     return inner_func

# odd = calculate()
# print(odd())

# Eg of a decorator
# def decorator_function(function_as_an_argument):
#     def wrapper_function():
#         print("Hello from the wrapper...")
#         return function_as_an_argument
#     return wrapper_function

# def show_message():
#     print("This message is from a decorator")

# Classes
#__repr__ is meant to be the unambigious representation of the object and soudl be used fo dedugging
#__str__ is meant to be more readable for the user.
# using @property allows us to use an function inside a class with self as an attribute. Eg
# class Employee:
# @property
# def email(self):
#     return "{}.{}@email.com".format(self.first, self.last)
#
# create an instance, emp_1 = Employee(.......)
# emp_1.email without ()

# Getters and Setters\
# Setters is a method that is used to set or change the value of private attributes
# Getters is a method that is used to access or get the value of the private attributes






