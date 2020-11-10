# create modules by making a file in the same folder and import the file using file name of module
# modules help to divide large codes in smaller manageable  form
# here i have created a separate file named cube_module which serves as a module
# after that i have imported the module by import cube_module
import cube_module

lisst = [1, 2, 3, 4, 5, 56]

print(cube_module.cube(3))
print(cube_module.mean(lisst))