# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.


# Learn Python with quick and easy examples
# Author: shrirangphadke@gmail.com

# Generators
# Generater is one of the easy yet very important tool in Python
# Consider a situation when you need to implement a long running
# generater function. For e.g. 100,000,00 UUID generater function
# Now how would you return the generated UUIDs? In a list? or dict?
# But that would need to hold UUIDs in memory for a log time. These
# type of scinarios are solved by the generater functions.
# Please find the example below:

#Example 1
import uuid

def uuid_funtion(x):
    while x:
        yield uuid.uuid1()
        x -= 1

for j in uuid_funtion(10):
    print j

# Above is the simplest implementation of generaters. Please pay
# attention to the keyword yield. Whenever we implement a function
# with yield keyword python automatically converts a function to
# a generater function. A Generater function reterns an iterater
# object. Using this iterater object we can fetch values one at a time
# Python iterators holds the state in which function was left and thus
# knows that exactly where it needs to start next time.

#Example 2
def uuid_infinite():
    while True:
        yield uuid.uuid1()

j = uuid_infinite()
# Since it is a generater function instead of going infinite it would
# return iterator for the uuid_infinite()

print j
# This prints:
# <generator object uuid_infinite at 0x7fda9871a3c0>

for itr in range(10): 
    print next(j)
