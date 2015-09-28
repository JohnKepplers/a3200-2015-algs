from random import randint
from sys import stdin, stdout

line = stdin.readline()
a = [int(j) for j in line.split()]
d = {}
'''test = [int(0) for i in range(0, 10000)]
for i in range(len(test)):
    test[i] = 2'''
counter = 0
for i in range(len(a)):
    if d.get(a[i]) == None:
        d.update({a[i]: 1})
    else:
        d[a[i]] += 1
ar = [0] * len(d)
for key in d.keys():
    ar[counter] = key
    counter += 1


def quick_sort(a, p, r):
    if p < r:
        q = randomised_partition(a, p, r)
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)


def randomised_partition(a, p, r):
    rand = randint(p, r)
    a[rand], a[r] = a[r], a[rand]
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] < x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


array = [0] * len(a)
j = 0
for key, value in d.items():
    array[j] = key
    j += 1
    for i in range(value - 1):
        array[j] = key
        j += 1

quick_sort(ar, 0, len(ar) - 1)
stdout.write(str(a))


