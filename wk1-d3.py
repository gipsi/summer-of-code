# 1 Million Women To Tech
# Summer of Code
# Week 1
# Day 3

# Notes

# Love Affair between Numbers and Letters

# See love.py

# name = ""
# print(name[0])
# print(name[-1])
# Traceback (most recent call last):
#   File "var.py", line 10, in <module>
#     print(name[])
# NameError: 'name' is not defined

name = "gipsi"
# print(name[0])
# print(name[-1])
# g
# i

#  ... ok ... I feel my brain working!

# Open a new tab in your Command Line and type python. # You should see >>> which means the computer is 
# listening for your python instructions. 

# This is nice for experimenting, just be careful 
# because your code is NOT saved anywhere.

# However, when you are testing behaviour of methods, # this is a quick way, because you don't have to type # print() all the time. 

# The interpreter will implicitly convert your result to a string and print it out for you.

# var1 = 2
# var2 = ​'5'​
# print(var1 + var2)
# Traceback (most recent call last):
#   File "<stdin>", line1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' # and 'str'

# Part of the problem is that your computer doesn’t 
# know if you were trying to get 7 (2 + 5) or if you 
# wanted to get 25 ('2' + '5'). But we’ll learn how to # do both.

# Before we can add these together, we need some way 
# of getting the string version of var1 or of getting # the integer version of var2.

# Conversions

# To get the string version of an object, we simply 
# use the str() method.

# var1 = 2
# var2 = ​'5'​
# print(str(var1) + var2)
# 25

# Vocabulary: programmers will say, we call the str() # method on variable var1.

# Some time on this next bit!
# I got three dots  like ...
# and invalid syntax error
# It didn't work in the interpreter so I went back to # printing the file.

# var1 = 2
# var2 = '5'
# print(str(var1) + var2)
# 25
# print(var1 + int(var2)
# SyntaxError: unexpected EOF while parsing
# print(var1)
# 2 yay!
# print(var2)
# 5 :))

# #####Reference: str(): 
# https://docs.python.org/3/library/stdtypes.html#str

# int(): 
# https://docs.python.org/3/library/functions.html#int

# float(): 
# https://docs.python.org/3/library/functions.html#float

# Python built-in functions: 
# https://docs.python.org/3/library/functions.html

# Try some more interesting (and a few just weird) # conversions:

# float('15')​
# SyntaxError: invalid character in identifier
# float(99.999'​)
# SyntaxError: EOL while scanning string literal
# int('99.999'​)            
# SyntaxError: invalid character in identifier

# int('5 is my favorite number!'​) 
# SyntaxError: invalid character in identifier
# int('Who asked you about 5 or whatever?'​)
# SyntaxError: invalid character in identifier
# float('Your momma did.'​)
# SyntaxError: invalid character in identifier
# str('stringy'​)
# SyntaxError: invalid character in identifier
# int(3)
# back to prompt

# feels like I'm missing something obvious

# with the syntax error messages the caret was 
# pointing to a space before the last bracket
# ... but there is no space :/

# So, this probably gave you some surprises.

# Explain what happened: what got converted, which 
# parts got ignored. What do the error messages say?

# Finally, we saw that our last two conversions did 
# nothing at all, just as we would expect.

# Another Look at print()

# There’s something strange about our favorite method. # Take a look at this:

# print(20)
# print(str(20))
# print(20)
# output:
# 20
# 20
# 20

# Well, here’s the big secret behind our friend 
# print(): before print() tries to write out an 
# object, it uses str() to get the string version of 
# that object.

# In fact, in Ruby print() is puts() and the s in puts # stands for string; puts really means put string.

# This may not seem too exciting now, but Python has 
# many, many kinds of objects (you’ll even learn how 
# to make your own), and it’s nice to know what will   # happen if you try to print a really weird object, 
# such as a picture of your grandmother or a music 
# file or something. It’ll always be converted to a 
# string first. But that will come later. In the 
# meantime, we have a few more methods for you, and 
# they allow us to write all sorts of fun programs.

# The input() Method

# If print() means print a string, I’m sure you can 
# guess what input() stands for. And just as print() 
# always spits out strings, input() retrieves only 
# strings. And whence does it get them?

# From you! Well, from your keyboard, anyway. And 
# since your keyboard makes only strings, that works 
# out beautifully. What actually happens is that 
# input() just sits there, reading what you type until # you press Enter.

# Let’s try it:

# >>>print(input())

  # ​Is there an echo in here?​
  # Is there an echo in here?

# Of course, whatever you type will just get repeated # back to you. Run it a few times, and try typing 
# different things.

# >>>print(input())
#  how much water do ponies drink?
#  how much water do ponies drink?

# A Few Things to Try

    # Full name greeting. Write a program that asks 
	# for a person’s first name, then middle, and then # last. Finally, it should greet the person using # their full name.

    # Bigger, better favorite number. Write a program # that asks for a person’s favorite number. Have 
	# your program add 1 to the number, and then 
	# suggest the result as a bigger and better 
	# favorite number. (Do be tactful about it, though.)

# Well here it is! I figured out how to do it, it took # some searches to get the spacing between the names 
# and it works - happy dance.

name1 = input('Enter your first name: ')
name2 = input('Enter your middle name: ')
name3 = input('Enter your last name: ')
print('Hello', name1 + ' ' + name2 + ' ' + name3)

bestnumber = input('Enter your favourite number: ')
print('Perhaps a better number is?', int(bestnumber) + 1)
