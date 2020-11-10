# you can raise exception using raise keyword

print("this is exception handeling with raise\n".upper())
number = int(input("enter a number "))

if number <0:
    raise Exception("number can,t be less than zero")

