from random import randint
from sys import stdin, stdout


def quick_sort(a, p, r):
    if p < r:
        first, last = randomised_partition(a, p, r)
        quick_sort(a, p, first)
        quick_sort(a, last + 1, r)
    return a


def randomised_partition(a, p, r):
    rand = randint(p, r)
    pivot = a[rand]
    counter = p
    first = p
    last = r
    while counter <= last:
        if a[counter] > pivot:
            a[counter], a[last] = a[last], a[counter]
            last -= 1

        elif a[counter] < pivot:
            a[counter], a[first] = a[first], a[counter]
            first += 1
            counter += 1
        else:
            counter += 1
    return first, last

if __name__ == '__main__':
    array = [int(i) for i in stdin.readline().split()]
    quick_sort(array, 0, len(array) - 1)
    stdout.write(str(array))
