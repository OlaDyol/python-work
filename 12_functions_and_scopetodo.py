"""
Working with functions and scope
"""

# TODO: Section 1:
# Define a function called "double" that sets a parameter of x. The function should double x and
# print that value inside the function. Call the function and pass it the below variable as
# an argument.
# double_this = 7
# def double(x):
#     x*=2
#     print(x)
# double(double_this)
#After completing the above, define a function called "printer", that sets no parameter.
# The function should just print the "double_this" variable. Call the function.

####################################################################################################

# TODO: Section 2:
# Copy your "double" function from above to this block of code.
# TIP: Comment out the previous definition of your "double" function before implementing this todo,
# TIP: as it is bad practice to have two function definitions with the same name.

# Change it to use a return value, store that return value in a variable, and print it.
# double_this = 3
# def double(x):
#     x*=2
#     return(x)
# print(double(double_this))

# FIXME: Paste function here
double_this = input("Please enter a day:")
def double(x):
    x*=2
    return(x) 
    
double = double(double_this)
####################################################################################################

# TODO: Section 2.1:
# Write an if statement that uses f shorthand to print either "{number here} is greater than 10" or
# "{number here} is less than 10" using the return value of your double function

if (double_this > 10 ):
    print (f"{double} is greater than 10"),
else:
    print (f"{double} is less than 10"),
