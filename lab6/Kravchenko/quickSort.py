from random import randint
from sys import stdin, stdout

line = stdin.readline()
a = [int(j) for j in line.split()]
d = {}
'''test = [int(0) for i in range(0, 10000)]
for i in range(len(test)):
    test[i] = 2'''


def crutch(a):
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
    if counter != 0:
        quick_sort(ar, 0, len(ar) - 1)
        counter = 0


def quick_sort(a, p, r):
    global h

    if p <= r:
        h = 0
    if p < r:
        h = 0
        q = randomised_partition(a, p, r)
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)
    if h == 0:
        another_crutch(a)
        h = 1




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


def another_crutch(a):
    counter = 0
    print(counter)
    for key, value in d.items():
        if d[key] > 1:
            counter += d[key] - 1

    array = [0 for y in range(len(a) + counter)]
    j = 0
    l = 0
    for key in d.keys():
        array[j] = a[l]
        j += 1
        l += 1
        for i in range(d[key] - 1):
            array[j] = key
            j += 1
    return print(array)



crutch(a)
