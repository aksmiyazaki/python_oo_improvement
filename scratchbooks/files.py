myfile=open('myfile.txt')
myfile.read()
myfile.read()
myfile.seek(0)
contents = myfile.read()
myfile.seek(0)
myfile.readlines()
myfile.close()

with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()

contents

with open('myfile.txt', mode='r') as myfile:
    contents = myfile.read()

with open('myfile.txt', mode='w') as myfile:
    contents = myfile.read()

with open('myfile.txt', mode='r') as f:
    print(f.read())
with open('myfile.txt', mode='a') as f:
    f.write('FOUR ON FOURTH')

with open('myfile.txt', mode='r') as f:
    print(f.read())

with open('asdfasdfasdf.txt', mode='w') as f:
    f.write('I CREATED THIS FILE!')

with open('asdfasdfasdf.txt', mode='r') as f:
    print(f.read())
