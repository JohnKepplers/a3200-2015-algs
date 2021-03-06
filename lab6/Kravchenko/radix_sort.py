from sys import stdin


def radix_sort(a):
    rang = 10
    counter = 0
    counter_positive = 0
    counter_negative = 0
    for i in range(len(a)):
        if a[i] < 0:
            counter += 1
    ar_positive = [0] * (len(a) - counter)
    ar_negative = [0] * counter
    for i in range(len(a)):
        if a[i] < 0:
            ar_negative[counter_negative] = -a[i]
            counter_negative += 1
        else:
            ar_positive[counter_positive] = a[i]
            counter_positive += 1

    if counter_positive > 0:
        y = 0
        z = max(ar_positive)
        while z > 0:
            z //= 10
            y += 1
        for i in range(y):
            b = [[] for k in range(rang)]
            for x in ar_positive:
                digit = (x // (10 ** i)) % 10
                b[digit].append(x)
            ar_positive = []
            for k in range(rang):
                ar_positive += b[k]
    if counter_negative > 0:
        y = 0
        z = max(ar_negative)
        while z > 0:
            z //= 10
            y += 1
        for i in range(y):
            b = [[] for k in range(rang)]
            for x in ar_negative:
                digit = (x // (10 ** i)) % 10
                b[digit].append(x)
            ar_negative = []
            k = 9
            while k >= 0:
                ar_negative += b[k]
                k -= 1
    for i in range(len(ar_negative)):
        ar_negative[i] *= (-1)
    for i in range(len(a)):
        a[i] = 0
    for i in range(len(ar_negative)):
        a[i] = ar_negative[i]
    for i in range(len(ar_negative), len(a)):
        a[i] = ar_positive[i - len(ar_negative)]
    return a


if __name__ == '__main__':
    ar = [int(i) for i in stdin.readline().split()]
    radix_sort(ar)
    print(ar)
