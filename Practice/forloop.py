#for loops
my_list = [1,2,3,4,5,6,7,8,9,10]

for num in my_list:
    print(num)

for num in my_list:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd Number')

list_sum = 0
for num in my_list:
    list_sum = list_sum + num

print(list_sum)

for _ in 'Hello World':
    print('Cool!')

tup = (1,2,3)
for item in tup:
    print(item)

my_new_list = [(1,2), (3,4), (5,6), (7,8), (9,10)]
len(my_new_list)

for item in my_new_list:
    print(item)

#tuple unpacking
for (a,b) in my_new_list:
    print(a)
    print(b)

my_other_list = [(1,2,3), (4,5,6), (7,8,9)]
for (a,b,c) in my_other_list:
    print(b)

d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d.items():
    print(item)

for key,value in d.items():
    print(value)

#same as above
for value in d.values():
    print(value)

#print number but not including max range
for num in range(10):
    print(num)

for num in range(3,10):
    print(num)

for num in range(0,11,2):
    print(num)

index_count = 0
for letter in 'abcde':
    print('At index {}, the letter is {}'.format(index_count, letter))
    index_count += 1

word = 'abcde'
for item in enumerate(word):
    print(item)

mylist1 = [1,2,3]
mylist2 = ['a','b','c']
zip(mylist1, mylist2)
for item in zip(mylist1, mylist2):
    print(item)