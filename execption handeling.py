# when dealing with inputs and some kind of specific errors we use exception handling
# suppose you want integer input from user but the user provides character input this will cause an error
# to prevent that error from happening we can use exception handling

# try, except, finally, raise , else are keywords used in exception handeling
# without 'try' 'except' will not work
# finally block lets you execute code, regardless of the result of the try- and except blocks


print("this is about exception handeling\n".upper())

try:
    number = int(input("enter an integer "))
except ValueError:
    print("Please enter an integer ")

try:
    number1 = int(input("enter an integer "))
except ValueError:
    print("Please enter an integer ")

try:
    Sum = number + number1
    print("The sum is {}".format(Sum))
except NameError:
    print("without numbers sum can,t be done")


