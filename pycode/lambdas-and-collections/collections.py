from functools import reduce

domain = [1, 2, 3, 4, 5]

our_range = map(lambda num: num * 2, domain)
print(list(our_range))

evens = filter(lambda num: num % 2 == 0, domain)
print(list(evens))

the_sum = reduce(lambda acc, num: acc + num, domain, 0)
print(the_sum)

words = ['Boss', 'a', 'Alfred', 'fig', 'Daemon', 'dig']
print("sorting by default")
print(sorted(words))

print("sorting with lambda key")
print(sorted(words, key=lambda s: s.lower()))

print("sorting with a method")
words.sort(key=str.lower, reverse=True)
print(words)