#Problem# 1: Strings, assignments and comments
#Let the variable x be "dog" and the variable y be "cat". Write the values returned by the following operations:
#a. x+y
# b.	"the " + x + " chases the " + y
# c. x * 4
x = "dog"
y = "cat"
print(x+y) #dogcat
print("the", x, "chases the", y) #the dog chases the cat
print(x*4) #dogdogdogdog

#Problem #2: Expressions Part 1
profit = 1000.55 # $1000.55
print('$', profit)
print('$' + str(profit))

#Problem# 3: Expressions Part 2
#Let x = 8 and y = 2. Write the values of the following expressions:
# a.x+ y * 3
# b.(x + y) * 3
# c. x ** y
#d. x % y
#e.	x / 12.0
#f. x // 6

x = 8
y = 2
print(x+ y * 3)#14
print((x + y) * 3)#30
print(x ** y)#64
print(x % y)#0
print(x / 12.0)#0.6666666666
print(x // 6)#1

#Problem #4: Expressions Part 3
#	Let x = 4.66 Write the values of the following expressions:
#a.round(x)
#b.int(x)

x = 4.66
print(round(x))#5
print(int(x))#4

#Problem #5: Using functions and modules
#The math module includes a pow function that raises a number to a given power.
#The first argument is the number, and the second argument is the exponent. 6,2
#Write a code segment that imports this function and calls it to print the values 8 to the power of 2 and 5 to the power of 4.

import math #we will import math library to use the math module
print(math.pow(8,2)) #pow is a function so we use the power function to raise a number.
print(math.pow(5,4))
print( 8 ** 2) #alternative way in calculating exponential form
print(5 ** 4)#alternative way in calculating exponential form