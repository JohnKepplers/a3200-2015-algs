from sys import stdin, stdout

first_line = stdin.readline()
a = [int(j) for j in first_line.split()]


def radix_sort(a, d):
    rang = 10
    for i in range(d):
        b = [[] for k in range(rang)]
        for x in a:
            digit = (x // (10 ** i)) % 10
            b[digit].append(x)
        a = []
        for k in range(rang):
            a += b[k]
    print(a)
radix_sort(a, len(str(max(a))))
