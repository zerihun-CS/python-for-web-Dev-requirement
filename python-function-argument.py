# In Python, you can define a function that takes variable number of arguments. 

# Function arguments can have default values in Python.

# We can provide a default value to an argument by using the assignment operator (=).
# Here is an example.

# Python Default Arguments
def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print("Hello", name + ', ' + msg)


greet("Kate")
greet("Bruce", "How do you do?")

print(greet.__doc__)



# Python Keyword Arguments

# 2 keyword arguments
greet(name = "Bruce",msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?",name = "Bruce") 

# 1 positional, 1 keyword argument
greet("Bruce", msg = "How do you do?")           


# Python Arbitrary Arguments

# Sometimes, we do not know in advance the number of arguments that will be passed into a function. 
# Python allows us to handle this kind of situation through function calls with an arbitrary number of arguments.


def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Rachel Green-Geller", " Monica Geller-Bing", "Phoebe Buffay-Hannigan", "Joey Tribbiani","Chandler Bing ","Ross Geller")