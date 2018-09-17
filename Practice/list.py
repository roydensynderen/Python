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