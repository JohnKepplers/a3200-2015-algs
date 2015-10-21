from sys import stdin, stdout


def median(a):
    if len(a) == 5:
        x = 0
        z = 3
        if a[1] > a[0]:
            x = 1
        if a[2] > a[x]:
            x = 2
        if a[3] < a[4]:
            z = 4
        if a[x] < a[z]:
            del a[z]
        else:
            del a[x]
    if len(a) == 4:
        if a[2] > a[3]:
            z = 2
        else:
            z = 3
        if a[0] > a[1]:
            x = 0
        else:
            x = 1
        if a[z] > a[x]:
            del a[z]
        else:
            del a[x]
    if len(a) == 3:
        if a[0] > a[1]:
            x = 0
        else:
            x = 1
        if a[2] > a[x]:
            x = 2
        return a[x]
    if len(a) < 3:
        return a[0]


testing_array = [int(i) for i in stdin.readline().split()]


def find_pivot(a):
    if len(a) == 1:
        return a[0]
    k = []
    j = 0
    array = [0] * (int((len(a) - 1) / 5) + 1)
    for i in range(0, len(a), 5):
        if len(a) - i >= 5:
            array[j] = median([a[i], a[i + 1], a[i + 2], a[i + 3], a[i + 4]])
            j += 1
        else:
            while len(a) - i > 0:
                k += [a[i]]
                i += 1
            array[j] = median(k)
    a = array
    return find_pivot(a)


stdout.write(str(find_pivot(testing_array)))
