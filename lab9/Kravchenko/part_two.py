from sys import stdin, stdout


def insertion_sort(a, p, r):
    for j in range(p, r):
        key = a[j]
        i = j - 1
        while i >= p and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key
    return a


k = int(stdin.readline())
testing_array = [int(i) for i in stdin.readline().split()]


def sorting(a):
    cr = []
    j = 0
    array = []
    for i in range(0, len(a), 5):
        if len(a) - i >= 5:
            array += insertion_sort([a[i], a[i + 1], a[i + 2], a[i + 3], a[i + 4]], 0, 5)
            j += 1
        else:
            while len(a) - i > 0:
                cr += [a[i]]
                i += 1
            array += insertion_sort(cr, 0, len(cr) - 1)
    return array


def find_pivot(a):
    if len(a) == 1:
        return a[0]
    sorting(a)
    j = 0
    array = [0] * (int((len(a) - 1) / 5) + 1)
    for i in range(0, len(a), 5):
        if len(a) - i >= 5:
            array[j] += a[i + 2]
            j += 1
        else:
            if len(a) - i == 4:
                array[j] += a[2]
            elif 1 < len(a) < 4:
                array[j] += a[1]
            else:
                array[j] += a[0]
    a = array
    return find_pivot(a)


def smart_partition(a, p, r):
    b = a
    pivot = b.index(find_pivot(a))
    a[pivot], a[r] = a[r], a[pivot]
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] < x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[r] = a[r], a[i + 1]
    return i + 1


def select(a, p, r, i):
    if p == r:
        return a[p]
    q = smart_partition(a, p, r)
    k = q - p + 1
    if i == k:
        return a[q]
    elif i < k:
        return select(a, p, q - 1, i)
    else:
        return select(a, q + 1, r, i - k)


if __name__ == '__main__':
    answer = []
    iterator = 0
    if len(testing_array) >= k:
        while iterator < k:
            answer += [select(testing_array, 0, len(testing_array) - 1, len(testing_array))]
            iterator += 1
            del testing_array[testing_array.index(answer[iterator - 1])]
        stdout.write(str(answer))

    else:
        stdout.write("length is less then k. Error!")
