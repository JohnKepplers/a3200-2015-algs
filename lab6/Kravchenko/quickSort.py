from random import randint
from sys import stdin, stdout
line = stdin.readline()
a = [int(j) for j in line.split()]


def quick_sort(a, p, r):
    if p < r:
        q = randomised_partition(a, p, r)
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)


def randomised_partition(a, p, r):
    i = randint(p, r)
    y = a[i]
    a[i] = a[r]
    a[r] = y
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] < x:
            i += 1
            y = a[i]
            a[i] = a[j]
            a[j] = y
    y = a[i + 1]
    a[i + 1] = a[r]
    a[r] = y
    return i + 1


quick_sort(a, 0, len(a) - 1)
stdout.write(str(a))
