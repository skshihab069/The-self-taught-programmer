my_dict = {}
print("This is your dictionary")
num = int(input("how many items do you need ?"))
for i in range(0,num):
    product = input("enter key")
    value = input("enter value")
    my_dict[product] = value

print(my_dict)
