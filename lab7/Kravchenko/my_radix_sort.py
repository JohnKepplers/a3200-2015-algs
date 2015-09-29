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
        for i in range(len(str(max(ar_positive)))):
            b = [[] for k in range(rang)]
            for x in ar_positive:
                digit = (x // (10 ** i)) % 10
                b[digit].append(x)
            ar_positive = []
            for k in range(rang):
                ar_positive += b[k]
    if counter_negative > 0:
        for i in range(len(str(max(ar_negative)))):
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

    print(ar_negative + ar_positive)
