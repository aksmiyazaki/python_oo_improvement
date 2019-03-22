my_dict = {'key1' : 'value1', 'key2': 'value2'}

my_dict['key1']

prices_lookup = {'apple' : 2.99, 'oranges': 1.99, 'milk': 5.80}
prices_lookup['apple']

d = {'k1':123,'k2':[0,1,2], 'k3':{'insidekey':100}}
d['k2']
d['k3']['insidekey']
d['k2'][2]

d.keys()
d.values()
d.items()

### Tuples
tupl = (1,2,3)
mylist = [1,2,3]

type(tupl)
type(mylist)
tupl[0]
tupl[-1]
tupl = ('1','1','2')
tupl.count('1')
tupl.index('1')
tupl[0] = 'NEW'

## Tuples are indicated when you want immutability

## Sets
## Unordered collections of unique elements
myset = set()
myset.add(1)
myset.add(2)
myset.add(2)
myset
