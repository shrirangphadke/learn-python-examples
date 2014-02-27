# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.


#Learn Python with quick and easy examples
#Author: shrirangphadke@gmail.com

#Simple squares
sq = [x**2 for x in range(10)]
print 'Sample square example'
print sq

#strings in a list
names = ['Bus', 'Train', 'Car', 'Bicycle']
print 'Leangth of each word'
print [len(name) for name in names]

print 'Last letter in each word'
print [name[-1] for name in names]

print 'String reverse for each word'
print [name[::-1] for name in names]

#map function on list
def square(no):
    return no**2

mlist = map(square, range(10))
print 'Simple map example'
print mlist

#lamba function example
mlist = map(lambda x: x**2, range(10))
print 'Simple lamda function example'
print mlist

#filter function example
#Filter takes a function returning True or False and applies it to a
#sequence, returning a list of only those members of the sequence for
#which the function returned True.
flist = filter(lambda x: x > 5 and x < 50, mlist)
print 'Simple filter function example'
print flist


#Filtered list comprehentions
#example 1
flist = [ x**2 for x in range(10) if x**2 > 5 and x**2 < 50 ]
print 'Filtered list comprehention example'
print flist

#example 2
print 'Filtered list comprehention example'
names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']
fnames = [name for name in names if name.startswith('B')]
print fnames
