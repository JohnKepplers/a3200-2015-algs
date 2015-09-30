from random import randint

d = {}


def crutch(a):
    ar = []
    for i in range(len(a)):
        if d.get(a[i]) == None:
            d.update({a[i]: 1})
            ar.append(a[i])
        else:
            d[a[i]] += 1
    print(ar)
    quick_sort(ar, 0, len(ar) - 1)
    print(another_crutch(ar))


def quick_sort(a, p, r):
    if p < r:
        q = randomised_partition(a, p, r)
        quick_sort(a, p, q - 1)
        quick_sort(a, q + 1, r)
    return a


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
    for i in range(len(a)):
        if d[a[i]] > 1:
            counter += d[a[i]] - 1

    array = []
    print(a)
    for l in range(len(a)):
        array.append(a[l])
        while d[a[l]] > 1:
            array.append(a[l])
            d[a[l]] -= 1

    return array

