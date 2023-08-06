x = 5
y = "Hello World"
print(y)

# print = "Hello World"

# Camelcase
# myVariableName = "Hello World 2"
# print(myVariableName)

# snakecase
my_variable_name = "Hello World 3"
print(my_variable_name)

# no reserved keywords for variable declaration

age, height, length = 18, 7.1, 6

print(age)
print(height)

# unpacking
fruits = ["apple", 'banana', "cherry"]
print(fruits[1])
# firstF, secondF, thirdF = fruits
# print(firstF)
# print(secondF)


# assigning a single value to multiple variables
green = big = Fruits = "mango"
print(green)
print(big)


# output variables
text = "Python is awesome"
secondText = "you should learn it"
print(text, secondText)


value1 = str(1) #casting
value2 = "string"
print(value1+value2)


#variable scope

'''
functions are basically a block of code that can be used
to excute or perform tasks
'''


#make a scoped variable global with the global [vairbale name]
#keyword
def myFunction():
    global functVar1
    functVar1 = "First function variable"
    print(functVar1)

myFunction()
print(functVar1)