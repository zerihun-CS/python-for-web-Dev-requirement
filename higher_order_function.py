# Higher Orders Functions are functions that perform operations on other functions

# A if it contains other functions as a parameter or returns a function as an output i.e,
# the functions that operate with another function are known as Higher order Functions


# Properties of higher-order functions:

#     A function is an instance of the Object type.
#     You can store the function in a variable.
#     You can pass the function as a parameter to another function.
#     You can return the function from a function.
#     You can store them in data structures such as hash tables, lists, …


# Functions as objects

# In Python, a function can be assigned to a variable. 
# This assignment does not call the function, instead a reference to that function is created. 
# Consider the below example, for better understanding.

# Python program to illustrate functions 
# can be treated as objects 
def shout(text): 
    return text.upper() 
    
print(shout('Hello')) 
    
# Assigning function to a variable
yell = shout 
    
print(yell('Hello'))

# Passing Function as an argument to other function

# Functions are like objects in Python, therefore, they can be passed as argument to other functions. 
# Consider the below example, where we have created a function greet which takes a function as an argument.

# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
    return text.upper() 
    
def whisper(text): 
    return text.lower() 
    
def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a function \
    passed as an argument.") 
    print(greeting)  
    
greet(shout) 
greet(whisper)


# Returning function

# As functions are objects, we can also return a function from another function.
# In the below example, the create_adder function returns adder function.
# Python program to illustrate functions 
# Functions can return another function 
    
def create_adder(x): 
    def adder(y): 
        return x + y 
    
    return adder 
    
add_15 = create_adder(15) 
    
print(add_15(10))

# Decorators

# Decorators are the most common use of higher-order functions in Python. 
# It allows programmers to modify the behavior of function or class. 
# Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it. In Decorators, 
# functions are taken as the argument into another function and then called inside the wrapper function.
