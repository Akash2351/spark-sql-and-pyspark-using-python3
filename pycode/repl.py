#!/usr/bin/env python3
from functools import reduce

a = 100
print(type(a))
a = "100"
print(type(a))
print(int(a))
type(int(a))

print("hello")
print(f"hello {a}")

l = range(1, 10)
res = 0
for i in l:
    if(i % 2 == 0):
        res += i

print(res)

res = 0
i = 1
while(i <= 10):
    res += i
    i +=1
print(res)

# functions
print("Using functions")
def sum(lb, ub):
    total = 0
    while(lb <= ub):
        total += lb
        lb += 1
    return total

total = sum(1, 10)
print(total)

print("Using lambda functions")
def sum(func, lb, ub):
    total = 0
    while(lb <= ub):
        total += func(lb)
        lb += 1
    return total

def id(i):
    return i
def sq(i):
    return i*i

total = sum(sq, 1, 10)
print(total)
total = sum(lambda i: i * 2, 1, 10 )
print(total)

print("using collections - list, set, dict")
l = [1, 2,3, 4, 5, 1]
s = set(l)
print(l)
print(s)
first = l[0]
print(4 in l)
sublist = l[2:5]
last = l[-1]
first_to_fifth_list = l[:5]
print(first, last, sublist, first_to_fifth_list)
l.pop(0)
l.count(1)
# index of 1 from 5th position
l.index(1, 0)
s2 = set([1,2,1,3,6])
s3 = s.intersection(s2)
s4 = s2.difference(s)
print(s, s2, s3, s4)
print(list(s)[0])

# dict
d = { 1:"hello", 2:"world"}
print(d[1], d[2])
d[2] = "folks"
print(d[1], d[2], d.keys(), d.values(), d.items())
print(d.get(1), d.get(3))


# map reduce filter
print("map reduce and filter")
list_num = range(1, 100)
total = 0
for i in list_num:
    if i%2 == 0:
        total += i*i

print(total)
# same with map reduce
f = filter(lambda i: i%2 == 0, list_num)
m = map(lambda i: i*i, f)
r = reduce(lambda total, element: total + element, m)
print(r)

# read file
orderItemsFile = open("./../data/retail_db/order_items/part-00000", "r")
oderItemsRead = orderItemsFile.read()
orderItems = oderItemsRead.splitlines()
print(orderItems[0:5])
orderItemsFilter = filter(lambda rec: int(rec.split(",")[1]) == 68880, orderItems)
orderItemsMap = map(lambda rec: float(rec.split(",")[4]), orderItemsFilter)
orderItemsRev = reduce(lambda total, element: total + element, orderItemsMap)
print(orderItemsRev)

