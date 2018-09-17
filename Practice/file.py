#creating a txt file

with open('file.txt', mode='w') as f:
    f.write('I created this file!')

with open('file.txt', mode='r') as f:
    print(f.read())
