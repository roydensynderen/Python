print('This is a string {}'.format('INSERTED'))
#Result: This is a string INSERTED

print('The {} {} {}'.format('fox', 'brown', 'quick'))
#Result: The fox brown quick

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
#Result: The quick brown fox

print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
#Result: The quick brown fox

#FLOAT FORMATING FOLLOWS '{value: width.precision f}'
result = 104.12345
print(result)
print('The result was {r:1.2f}'.format(r=result))

#Another way to do it; released in Python 3.6
name = "Jose"
print(f'Hello, his name is {name}')

