
#################STRING####################STRING#################

new_list = ['one', 'two', 'three', 'four', 'five']

new_list[0] = "ONE IN CAPS"

another_list = ['six', 'seven', 'eight', 'nine', 'ten']

my_list = new_list + another_list

my_list1 = my_list[1:]

my_list.append('eleven')

my_list.pop()

num = [1, 3, 61, 23, 13, 25]

chare = ['t', 'w', 'e', 'q', 'y', 'j', 'g', 'j']

num.sort()
chare.sort()

chare.reverse()

num.reverse()

###############DICTIONARY############DICTIONARY###############

my_dict = {'key1' : 'value1', 'key2' : 'value2'}

prices_lookup = {'apple' : 2.99,'oranges' : 1.99, 'milk' : 5.80}

d = {'k1' : 123, 'k2' : [0,1,2], 'k3' : {'insidekey' : 100}}

d2 = {'key1' : ['a', 'b', 'c']}

mylist = d2['key1']

letter = mylist[2]

upperc = d2['key1'][2]

d3 = {'k1' : 100, 'k2' : 200}

d3['k3'] = 300

##############TUPLES#########TUPLES##############

t = (1,2,3)

mylist = [1,2,3]

t2 = ('one', 2)

t1 = ('a','a','b')

mylist3 = [1,2,3]

##########SETS##############SETS###############

myset = set()

myset.add(1)

myset.add(2)

mylist = [1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]

set(mylist)

#print(set(mylist))

###########BOOLEANS#########BOOLEANS###############

b = None


##########IO with Basic Files in Python###########IO##

myfile = open('forInputandOutput.txt')

#print(myfile.read())
myfile.seek(0)
#print(myfile.read())
myfile.seek(0)
#print(myfile.read())
contents = myfile.seek(0)
myfile.seek(0)

print(myfile.readlines())

















