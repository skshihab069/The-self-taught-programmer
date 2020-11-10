# String are iterable
# string is indexed starting with index 0
# "shihab" has index[0]=s, index[1] = h,  index[2]=i, index[3]= h, index[4] = a, index[5] = b
# "shihab" has index[-1]=b, index[-2] = a,  index[-3]=h, index[-4]= i, index[-5] = h, index[0] = s (reverse string traversing)

print("shihab" + " is" + " good_boy")  # This is called concatenation
print("love Urmi\n" * 3)  # you can multiply strings by multiplication oparator & you can use |n to create new line
print("shihab is soo cool".upper())  # makes the string upper case
print("SHIHAB IS SOO COOL".lower())  # makes the string lower case
print("shihab is soo brave ".capitalize())  # capitalizes the string
print("shihab said \"this was his resume\"")  # this called Escaping by using \ you can print quote symbols

################  THE FORMAT FUNCTION#######################
print("Programming is soo {} and soo {}".format("cool", "fun"))  # the format function is useful for getting user input
a = input()
b = input()
print("programming is soo {} and {}".format(a, b).capitalize())  # example of getting user input in string

################## THE SPLIT METHOD ########################
print("I Love Python. Because is soo easy. It is used in soo many fields like web dev and machine learning".split("."))
# The split method splits the strings in separate strings in a list of strings

################# THE JOIN METHOD ##########################
string = "shihab"
new = "@".join(string)
# the join method adds a charecter after each charecter in string and replaces with particular string
print(new)

################ JOINING STRINGS FROM LIST ##################
list_of_string = ["shihab", "is", "smart"]
new1 = " ".join(list_of_string)
print(new1)

############### STRING SLICING ###############################

string1 = "hello there"

print(string1[3:9])  # string[starting index : ending index]
print(string1[:])  # prints the entire string
print(string1[:11])  # slices till the end of string

############## THE REPLACE METHOD ##########################
string2 = " hey how you doing harley"
print(string2.replace("h", "@"))

############## FINDIND THE INDEX ##########################
string3 = "hey whats up my man, how you doin"
print(string3.index("m"))
