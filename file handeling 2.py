string = open("new_string.txt","w")
string.write("hello\n")
string.write("My name is Saief\n")
string.write("I am a Hybrid Engineer\n")
string.write("I know programming and networking")
string.close()

list = []
with open("new_string.txt","w") as f:
    f.write("hey this is new text ")
    f.write("how are you")
    f.write("i am awesome")
with open("new_string.txt","r") as r:
    list.append(r.read())

print(list)

