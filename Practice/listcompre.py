#Create a list from 1 - 50 that is divisible by 3
print [x for x in range(1,51) if x%3 == 0]

#Create a list of the first letter of every word in string
st = 'Create a list of the first letters of the word in this string '
print [word[0] for word in st.split()]