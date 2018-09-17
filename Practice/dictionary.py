#dictionary = objects in JS'

my_dict = {'key1':'value1', 'key2':'value2'}
print my_dict['key1']
#Result: 'value1'

#Access keys nested in a dictionary
d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':100}}
print d['k2']
print d['k3']
print d['k3']['insideKey']

#Changing a value in a list to upper case
new_d = {'key1': ['a', 'b', 'c']}
my_list = new_d['key1']
print my_list
letter = my_list[2]
print letter.upper()

#5 steps to 1 line
print new_d['key1'][2].upper()

#Adding a key value pair into a dictionary
existing_d = {'k1':100, 'k2':200}
existing_d['k3'] = 300
print existing_d

#Editing a value
existing_d['k1'] = 'NEW VALUE'
print existing_d

#Return all keys
print d.keys()

#Return all values
print d.values()

#Return all key value pairs
print d.items()
