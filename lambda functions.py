# A lambda function is a small anonymous function.
# lambda function can take any number of arguments, but can only have one expression
# lambda arguments : expression
# The power of lambda is better shown when you use them as an anonymous function inside another function
# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number


def double_the_number(num):
    return lambda a : a*num

double = double_the_number(2)

print(double(11))