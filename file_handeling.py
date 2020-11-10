# the open function returns a file object
# every open function needs a closing function

string = open("string.txt", "w")
string.write("i am an engineer, hello")
string.close()

# the alternative way is to use with statement, it performs an action automatically after execution
# you can access the file object with a variable, here i,m using  f
# you can use the read function only once you open a file soo you have to save it in a variable or list
my_list = []

with open("string.txt", "w") as f:
    f.write("i am a python expert")

with open("string.txt", "r") as r:
    my_list.append(r.read())

print(my_list)