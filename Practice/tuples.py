#immutable
#less flexible than a list
#less methods for tuple

#count how many times 'a' occurs in a tuple
t = ('a', 'a', 'b')
print t.count('a')

#checking the index for the first time it appears in a tuple
print t.index('a')
print t.index('b')