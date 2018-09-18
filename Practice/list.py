#list = array in JS
new_list = ['one', 'two', 'three', 'four', 'five']
print new_list[0]

new_list[0] = 'ONE WITH CAPS'
print new_list
#['ONE WITH CAPS', 'two', 'three', 'four', 'five']

#Add last item to list
new_list.append('six')
print new_list

#Remove last item from list
print new_list.pop()
popped_item = new_list.pop()
print popped_item
print new_list

alphabet_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4, 1, 8, 3]

alphabet_list.sort()
print alphabet_list

num_list.sort()
my_sorted_num_list = num_list
print num_list

my_string = 'hello'
my_list = []
for letter in my_string:
    my_list.append(letter)
print my_list

#same as above
my_list = [letter for letter in my_string]
print my_list

celcius = [0, 10, 20, 34.5]
fahrenheit = [( (9/5)*temp + 32 ) for temp in celcius] 
print fahrenheit

results = [x if x%2 == 0 else 'ODD' for x in range(0, 9)]
print results