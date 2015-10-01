from random import randint


def positive_and_negative_random_list(length):
    a = [randint(-1000000, 1000000) for i in range(length)]
    return a


def positive_random_list(length):
    a = [randint(0, 10000) for i in range(length)]
    return a


def strange_sorted_list(length):
    j = 0
    a = [0 for i in range(length)]
    a[0] = randint(0, 10000)
    l = 1
    while l < length:
        if j % 8 <= 3:
            p = randint(0, 10000)
            if p > a[l - 1]:
                a[l] = p
                j += 1
                l += 1
            else:
                continue
        if j % 8 > 3:
            p = randint(0, 10000)
            if p < a[l - 1]:
                a[l] = p
                j += 1
                l += 1
            else:
                continue

    return a


def normal_sort_list(length):
    a = positive_random_list(length)
    a.sort()
    return a


def abnormal_sort_list(length):
    a = normal_sort_list(length)
    return a[::-1]


def boring_list(length, number):
    a = [number for i in range(length)]
    return a
