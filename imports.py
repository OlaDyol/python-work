# Then, to access the constant `DAYS_OF_WEEK` from that file,
# you would do so with "dot notation" just like in section 1. In this import case,
# we can find the constant by using:
print(f"Normal dot notation: {importable_stuff.DAYS_OF_WEEK}")
print(f"Normal dot notation: {importable_stuff.DAYS_OF_WEEK}")  # TIP:
                                                                # DAYS_OF_WEEK is a list. In
                                                                # Python, lists are represented by
                                                                # items separated by commas inside
                                                                # open and closed brackets. Open
                                                                # importable_stuff.py to check this
                                                                # out.

# You could also rename imports such as:
import importable_stuff as stuff # Now this import can be referred to going forward as "stuff".
"""
Use compounding interest rates and initial investment to find your return on investment
and calculate the taxes owed
"""

# INSERT IMPORT STATEMENT HERE # FIXME

# TODO: Section 1
# Import the annual_interest and TAX_RATE constants from the file "interest.py" in
# studentrepository/todos/1_basics

# Ask a user how much they would like to invest with an input. Set it equal to a variable
# named "investment".
# TIP: Don't forget to convert the input to an integer!

# Calculate how much their investment would appreciate in one year by multiplying
# the investment variable by the annual_interest. Set the appreciation amount
# equal to a variable named "appreciation".

# TODO: Section 1.1

# Create a new variable named "new_value" by adding the "appreciation" variable to the
# "investment" variable.

# Calculate the taxes you have to pay by setting a variable of "taxes" equal to
# the "appreciation" variable times the TAX_RATE.

# Print to the user the following output using f shorthand: "Your investment of {investment} is now worth
# {new_value} and you owe {taxes} in taxes."
 4  lessons/students/10_imports/importable_stuff.py 
@@ -0,0 +1,4 @@
DAYS_OF_WEEK = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

SEASONS = ["Summer", "Fall", "Winter", "Spring"]
 3  lessons/students/10_imports/interest.py 
@@ -0,0 +1,3 @@
annual_interest = .0725
TAX_RATE = .20

 28  lessons/students/8_variables_and_types/8_variables_and_types.py 
@@ -45,7 +45,7 @@

# You don't have to create a variable to print an output. You can put strings directly into print
# statements!!
print("Hello my name is robot")
print("I am Groot")

# When you see, TODO: Section x of TODO y, you should stop where you are and head over to
# the corresponding assignment for this section of the lesson. The line below instructs
@@ -151,3 +151,29 @@
# Boolean: bool()

# TODO: Section 5 of TODO 2 (5 minutes for students, 3 minute demo)

####################################################################################################

# TITLE: Section 6 - "f shorthand"(3 minutes)

# Here we will introduce the primary method with which we will be inserting variables directly
# into strings, called "f shorthand". Let's set some variables and insert them in a string that has
# a lowercase "f" right before the first quotation mark in the string.

student1, student2, student3 = "Maria", "Sam", "Chris"

attendance_output = f"The present students are {student1}, {student2}, and {student3}."
print(attendance_output)

# "f shorthand" also implements type conversion in its execution. Any variable used inside f shorthand
# will be converted to a string in the output of a print statement. Let's see how "f shorthand"
# handles integers and strings together.

num1, num2, num3 = 7, 8, 9
print(f"Why was 6 afraid of {num1}?")
print(f"Because {num1} {num2} {num3}!")

# TAKEAWAY:
# "f shorthand" makes it easy to print outputs without needing to go through type conversion. In
# the above examples, "f shorthand" handles strings perfectly fine as well as the ability to handle
# strings and integers together without needing to concatenate. 
 59  lessons/students/8_variables_and_types/8_variables_and_typestodo.py 
@@ -0,0 +1,59 @@
"""
Using variables and types
"""

# TODO: Section 1:
# Set a variable 'phrase1' euqal to "Hi everyone! " and another variable 'phrase2'
# equal to "My name is [name here]". Then use what you learned so
# far in the lesson to set these varibles to a new variable called "complete"
# and print it.

####################################################################################################

# TODO: Section 2:
# Set two variable in the same line, "flt1" and "flt2", equal to 3.5 and 14.0, respectively.
# Then print each variable to check the output.

####################################################################################################

# TODO: Section 3:
# Set a variable called name equal to your name, then set a variable of age
# equal to your age as an integer. Print a statement with an output of
# "My name is [name here] and I am [age here] years old." using the above
# variables in your print statement.

# Takeaway:
# Concatenation (+) can only be done with strings, not strings and integers/floats. Commas, however,
# simply print different elements rather than attempting to concatenate strings.

####################################################################################################

# TODO: Section 4:
# Set a variable equal to each of the types we have learned so far. That includes
# integers, floats, booleans, None, and strings. So, have one variable per each
# of those types (i.e. exampleInt = 0, exampleBool = False, etc.).
# To check the type of something in python, you use the type() function.
# For example, type("Hello") would yield string, and type(6) would yield int.
# So, create on print statement that would print the type of each variable you've set.

# Takeaway:
# Types are important in Python and you can check different elements' types using type().
# The type() function is an example of a polymorphic function, meaning that the same
# function name can be used for different types.

####################################################################################################

# TODO: Section 5:

# Lastly, we will introduce type conversion. There are functions you can use to
# convert things in Python. The first type conversion function we will use is str().
# Try the problem from Section 3, but use plus signs to concatenate strings and
# print "My name is [name here] and I am [age here] years old." using the name and age
# variables. However, this time when you're concatenating the age variable, wrap it in the
# str() function as such: str(age). The print statement will no longer throw an
# error 🎯 since age was converted to a string.

# Takeaway:
# We can change types in Python when appropriate, and we learned one way to do so with str()

# Good job, everyone! First todo down 💪🏾
 52  lessons/students/9_basic_math/9_basic_mathtodo.py 
@@ -0,0 +1,52 @@
"""
Lets calculate a company's taxes, profit, and then divide the profit amongst shareholders.
"""

# TODO: Section 1:
# TIP: Use print statements to test your code along the way.

# Set the following variables and constants:
# Set a constant of "TAX_RATE" equal to .20 (we will use this as twenty percent).

# Receive a user input for the question "What was your revenue for this year?". Set
# the input equal to a variable called "revenue".
# HINT: What varible type do you want "revenue" to be?

# Set a variable equal to "taxes_paid". Calculate the taxes by multipling the rate (20%)
# from your previous variable by the revenue input from the user.

# Set a new variable called "profit". Calculate the revenue minus the taxes paid and set it
# equal to this variable.

# In this lesson we went over changing the value of a variable. In this example, your company
# is taking a one time charge of 50%. This is done by executing the following:
# profit = profit / 2 #IMPORTANT: Uncomment this line before moving on.

# TODO: Section 1.1:
# Print an output indicating "Company ____ recorded $______  in revenue this year,
# paid $______ in taxes, recorded a profit of $______, and paid $______ to their five
# shareholders, evenly". Be sure to format to look like normal dollar amounts - "$xx.xx"
# HINT: 
# To format decimal points to show only to the nearest hundreth, you must add ":.2f" after a
# variable is inserted. This would look like "{var_name:.2f}". So if var_name is equal to 4.837478,
# then the output would be "4.84".

# TAKEAWAY:
# 1) Variables that have input functions stored in them will be of the string type. To use them in
#    math operations, you must convert them to an integer or float.
# 2) You can alter the value of a variable by setting it equal to an operation on itself.
#    example: x = x * 2.

####################################################################################################

# TODO: Section 2:
num_list = [35, 4, 20, 100, 96]
# Set the minimum, maximum, and sum of num_list to the variables "min_num", "max_num", and
# "sum_list" respectively. Then print each in their own print statement in the format
# "The ___ of num_list is ___." using f shorthand.

# TODO: Section 2.1:
num_list2 = [-20, 15, -27, -11]
# Find the sum of num_list2 and store it in the variable "sum2". Then print the sum in the format,
# "The sum is ___". Then using f shorthand, return the value of the absolute value of "sum2" and
# print in the format, "The absolute value of sum2 is ___".