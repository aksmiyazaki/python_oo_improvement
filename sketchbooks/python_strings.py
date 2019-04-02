
batata = "cebola"
batata[2]
batata[0:3]
batata[0::2]
print(batata)

phrase = 'Bacon \'n Zitos'
phrase

len(phrase)

my_string = "Hello World"
my_string

my_string[0]
my_string[8]
my_string[9]
my_string[-2]

my_string = 'abcdefghijk'
my_string[2:]
my_string[:3]
my_string[3:6]
my_string[1:3]
my_string[::2]
my_string[2:7:3]
my_string[::-1]

name = "Sam"
## Code doesn't work, strings are immutable
#name[0] = 'P'
last_letters = name[1:]
last_letters = 'P' + last_letters
last_letters

x = "Hello World"
x  = x + " it is beautiful outside"
letter = 'z'
letter * 10
'2' + '3'
# Errror -> '2' + 3
x = "Hello World"
x.upper()
x.lower()
x.split()

x = 'Hi this is a string'
x.split()
x.split('i')

#.format method.
print("This is a string {}".format("INSERTED"))
print("The {2} {1} {0}".format('fox', 'brown', 'quick'))
print("The {q} {b} {f}".format(f='fox' ,b='brown', q='quick'))

result = 100/777
result
print("The result was {r:2.5f}".format(r=result))

result = 100/777
result
print("The result was {r:01.5f}".format(r=result))

name = "Jose"
print(f"Hello, his name is {name}")
