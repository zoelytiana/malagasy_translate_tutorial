"""
This is a simple calculator program.
Exercise:
1. Make sure it works correctly.
2. Fix any problems with this program
3. Commit the fix to your repository
3. Add feature to use existing subtraction function
4. Commit
5. Add multiplication and division (requires writing new function)

"""
def add_two_numbers(x,y):
    """ Adds two numbers """
    return x + y

def sub_two_numbers(x,y):
    """ subtract two numbers """
    return x - y
	
def mul_two_numbers(x,y):
    """ Multiplication two numbers """
    return x * y

def div_two_numbers(x,y):
    """ division two numbers """
    if y == "0":
        return "division by 0"
    return x / y

#Greeting
print("Hello! This is a simple program for simple calculations")

#Specify operation
doToday = input("What would you like to do today?")
#doToday = "add" #HACK
print("We will " + doToday + " two numbers now.")

var1 = int(input("First number: "))
var2 = int(input("Second number: "))

if doToday=="add":
    result = add_two_numbers(var1, var2)
	
if doToday=="sub":
    result = sub_two_numbers(var1, var2)

if doToday=="mul":
    result = mul_two_numbers(var1, var2)
	
if doToday=="div":
    result = div_two_numbers(var1, var2)
	
print("This is the result:", result)
print("I hope it is correct...")
print("Bye, now!")
