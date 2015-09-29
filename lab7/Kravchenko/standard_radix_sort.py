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
