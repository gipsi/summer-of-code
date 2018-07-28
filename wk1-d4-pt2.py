
# Saturday 28th July, 08:08  2018
# My intention this weekend isto catch up as much as I # can.  Getting the code to work as well as 
# understanding why it does is taking a more time than # I'd like and causing frustration.  It makes me 
# question that I can do it.

# a good reason not to copy and paste
# input = ''
# while input != ​'bye'​:
#   input = input()

# print(​'Come again soon!')​
# The first error thrown ...
#  File "moo.py", line 145
#     input = ''
#             ^
# SyntaxError: invalid character in identifier
# this reminds me of the anecdode of searching for 
# invisible bugs!

# input = ''
# while input != 'bye':
#   input == input()
  
# print('Come again soon!')

# ok I typed it out myself this time and still get 
# SyntaxError: invalid character in identifier 
# along the while line (fourth time)

# a search ...
# 1 Python the Hard way ( you have to pay unless you 
# go to the Ruby version)
# W3schools on while loops
# Stack overflow - hidden characters

#  input = ""
#  while input != "bye":
#    input = input()
  
# print("Come again soon")

# I keep getting the 
# SyntaxError: invalid character in identifier 
# with a # in front of the while line

# text = ""
# while text != "bye":
#   text = input("say something please : ")
#   print("you said" + text + ".")
  
# print("good bye to you too")

# I wrote the code in a new file and it works!
# copy and pasted it here and the hidden hash still 
# lurks 

# aha moment! The error was thrown on line 148
# an invisible character from copy and paste
# there was another on on line 50

# now the code above works again, yay!

# still not getting this code to work though:

# input = ''
# while input != 'bye':
#  input == input()
  
# print('Come again soon!')

# Subtle errors which may cause some fairly difficult 
# to follow messages happens when built-in type and 
# function names are "shadowed" (ie. redefined). For 
# example, using str as a variable name in a scope 
# (ie. a function or class) will prevent the built-in # function of the same name from being usable, 
# producing an error like this: TypeError: 'str' 
# object is not callable
# https://wiki.python.org/moin/BeginnerErrorsWithPythonProgramming

# moving on ...

# I don't know the 99 bottles song
# I know the 10 green bottles one

# look it up

# http://www.99-bottles-of-beer.net/

# for quant in range(00, 0, -1):
#    if quant > 1:
#       print (quant, "bottles of beer on the wall,", quant, "bottles of beer.")
#       if quant > 2:
#          suffix = str(quant - 1) + " bottles of beer on the wall."
#       else:
# 	     suffix = "1 bottle of beer on the wall."
# 	elif quant == 1:
# 	   print ("1 bottle of beer on the wall, 1 bottle of beer.")
# 	   suffix = 'no more beer on the wall!'
# 	print ("Take one down, pass it around,", suffix)
# 	print ("--")
	
# nope python 2 - tried to convert but:

# TabError: inconsistent use of tabs and spaces in indentation - line 235

# https://rosettacode.org/wiki/99_Bottles_of_Beer/Python#Using_a_generator_expression_.28Python_3.29

# This code worked when I got the spacing right!
 
def sing(b, end):
    print(b or 'No more','bottle'+('s' if b-1 else ''), end)
 
for i in range(99, 0, -1):
    sing(i, 'of beer on the wall,')
    sing(i, 'of beer,')
    print('Take one down, pass it around,')
    sing(i-1, 'of beer on the wall.\n')
	
# the "Hello World" of programming paradigms
#
