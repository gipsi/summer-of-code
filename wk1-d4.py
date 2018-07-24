# 1 Million Women To Tech
# Summer of Code
# Week 1
# Day 4

# moo.py

# The seven step approach to solving programming problems
  
# https://www.coursera.org/lecture/java-programming/solving-programming-a-seven-step-approach-IpUp4

# Two versions!

# https://www.coursera.org/lecture/duke-programming-web/a-seven-step-approach-to-solving-programming-problems-AEy5M

# 1 Work by example
# 2 Write down what you did
# 3 Find patterns
# 4 Check by hand
# 5 Translate to code
# 6 Run test cases
# 7 Debug test cases

# Looping

# while loop
# input = ''
# while input != 'bye':
# input = input()
  
# print('Come again soon!')

# I got an error message:
# TypeError: 'str' object is not callable

# went back to watch video

# text = ""
# while text != "bye";
# text = input("say something please")
#  if text == "bye":
#    print("good by to you to!")

# haha - SyntaxError: invalid syntax ... semicolon!

# text = ""
# while text != "bye":
#  text = input("say something please")
#  if text == "bye":
#   print("good by to you to!")
	
# yep that works (no space after the "say something 
# please" though)

# i = 1 
# while i < 11:
#   print(i) 
#   i = i + 1
  
# NOTE: without the incremental 1 the loop would run indefinately as ! would always be less than 11 which would not be good

# j = 0
# while j < 11:
#   print(j)
#   if j == 3:
#     break 
#   j += 1  
# good to put in break clause to prevent #infinite loop	
# this is syntax sugar as it could be   #written j = j + 1

# It did stick in a n ifinit loop of 00000 ... zeros  and I had to shut the shell - Why???

# I had commented out the first bit of code
# ... same again, next ... spot the difference!
# and the last line (61) was indented level with break

# DaDa! Now it works - good.
 
#  if your condition is not being met you are 
# executing it too early or too late eg:
# j = 0
# while j < 11:

#   if j == 3:
#     break 
#    print(j)
#    j += 1

# Now for some more text

text = ""
while text != "bye":
  text = input("say something please"" ")
  print("you said" + text + ".")
if text == "bye":
  print("good by to you to!")

# Nice the way the text editor hightlights if indent 
# is wrong.

# somehow I lost some lines in the editor so had to 
# undo them to get back - time for a break!
