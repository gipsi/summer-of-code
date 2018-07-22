# 1 Million Women To Tech
# Summer of Code
# Week 1
# Day 2
# Letters


print('Hello, World!')
# print('')
print('Good-bye.')

# Dig it - massaaa!

# print('I like' + 'apple pie.')

# I likeapple pie.  No spaces!

# Take two:

print('I like ' + 'apple pie.')
print('I like' + ' apple pie.')

print('blink ' * 4)

# And you get this:

# batting her eyes

# (Just kidding... not even Python is that clever.)

# blink blink blink blink

print(12 + 12)
print('12' + '12')
print('12 + 12')
# 24
# 1212
# 12 + 12

print(2 * 5)
print('2' * 5)
print('2 * 5')
# 10
# 22222
# 2 * 5

# Problems
# print('12' + 12)
# Traceback (most recent call last):
  # File "string.py", line 41, in <module>
    # print('12' + 12)
# TypeError: Can't convert 'int' object to str implicitly
# This is the example error message, I got a different one:
# TypeError: can only concatenate str (not "int") to str

# print('2' * '5')

# accidentally typed 'print string.py' instead of 
# python string.py in PowerShell got this message:
# Unable to initialize device PRN

# Next I got the error message from:
# print('12' + 12)
# three times.
# Then I remembered the mention of python stopping at # an error.

# After commenting it out I got:
# Traceback (most recent call last):
#  File "calc.py", line 48, in <module>
#    print('2' * '5')
#TypeError: can't multiply sequence by non-int of type # 'str'

# so ....

# you can't add a number to a string or multiply a string by another string.

# print('Betty' + 12)
# print('Francesca' * 'Hanna')
# Traceback (most recent call last):
  # File "string.py", line 70, in <module>
    # print('12' + 12)
# TypeError: can only concatenate str (not "int") to str

# Something else to be aware of: you can write 'pig'*5 # in a program, since it just means five sets of the # string 'pig' all added together. However, you can’t write 5*'pig', since that means 'pig' sets of the number 5, which is... poetic, at best.

print('pig'*5)

print(5*'pig')

# output:
# pigpigpigpigpig
# pigpigpigpigpig
# hmmm

# finally:
# print('You're swell!')
#   File "string.py", line 89
 #   print('You're swell!')
 #               ^
# SyntaxError: invalid syntax
# We need a way to tell the computer “I want an apostrophe here, inside this string.”

# How do we let the computer know we want to stay in 
# the string? We have to escape the apostrophe, like 
# this: 
print('You\'re swell!')
# ah another error message!
# file "string.py", line 92
#   ^
#   ^
# IndentationError: unexpected indent
# it was the caret, I had to comment it out

# Escape characters must always escape themselves. Why?

# The backslash is the escape character. In other 
# words, if you have a backslash and another 
# character, they are sometimes translated into a new # character.

# The only things the backslash escapes, though, are 
# the apostrophe and the backslash itself. (If you 
# think about it, escape characters must always escape # themselves, too, to allow for the construction of 
# any string. Why is that?)

# Let’s see a few examples of escaping in strings:
print('You\'re swell!')
print('backslash at the end of a string: \\')
print('up\\down')
print('up\down')
# You're swell!
# backslash at the end of a string: \
# up\down
# up\down

# Since the backslash does not escape a d but does 
# escape itself, those last two strings are identical. # Obviously they don’t look the same in the code, but # when your program is actually running, those are 
# just two ways of describing identical strings.

# You good so far? Good. Let’s start doing something 
# slightly more clever...

# Variables and assignment

print('...you can say that again...')
print('...you can say that again...')
# ...you can say that again...
# ...you can say that again...

# Principle: "Don't repeat yourself"

# Principle: "When coding be lazy. Not just lazy, but # agressively, proactively lazy."

# To store the string in your computer’s memory for 
# use later in your program, you need to give the 
# string a name.

# Programmers often refer to this process as 
# assignment, and they call the names variables.

# A variable name can usually be just about any 
# sequence of letters and numbers, but in Python the 
# first character of this name needs to be a lowercase # letter.

# Let’s try that last program again, but this time I 
# will give the string the name my_string (though I 
# could just as well have named it str or 
# myOwnLittleString or henry_the_8th):
my_string = '...you can say that again...'
print(my_string)
print(my_string)
# ...you can say that again...
# ...you can say that again...
