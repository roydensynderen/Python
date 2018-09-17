#Set does not allow addition for repeated value, only unique values

my_set = set()

#Adding something to a set
my_set.add(1)
print my_set

my_set.add(2)
print my_set

my_list = [1,2,1,2,1,2,1,2,1,2,1,2,3]
print set(my_list)
