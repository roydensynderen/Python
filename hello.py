print('Hello World')

myString = 'abcdefghi'
print myString[3:6]
#Result: def

#start stop step-size
print myString[2:7:2]
#Result: ceg

findDogInString = 'abcdefdoghijkl'
dogString = findDogInString[6:9]
print dogString

jumpCharByTwo = 'abcdefg'
print jumpCharByTwo[::2]
#Result: aceg

#Finding length of string
print len(dogString)

subString = 'abc12345'
print subString[3:]
#12345
print subString[:3]
#abc

reverseStr = 'royden'
print reverseStr[::-1]

