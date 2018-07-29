# week 2 Day 4

# Modules and packages

# Modules basics

# access to function and variable

# import cool_int as ci

# ci.to_eng(5)
# ci.to_eng(42)

# c = ci.awesome_student["city"]
# print(c)

# This worked first time!

# There are two more ways to do it shorter:

import cool_int

cool_int.to_eng(5)

import cool_int as ci

ci.to_eng(42)

from cool_int import to_eng
to_eng(6)

c = ci.awesome_student["city"]
print(c)

# install fest

# pip, Jupyter notebook and NLTK (without Anaconda)

# Check pip
# https://pypi.org/project/pip/



# Install NLTK
# ! Find the downloader !
# http://www.nltk.org/install.html
# This took a while understanding what to do about the 
# errors that showed up in Jupyter
# A useful page for downloading the data:
# http://www.nltk.org/data.html

# a downloader popup appeared from terminal after typing:
# >>> import nlk
# >>> nltk.download ()
# NOTE: on the downloader For central installation, set this # to C:\nltk_data (Windows)
# It would have been a lot quicker if I found this page earlier

# TB = tab proliferation
