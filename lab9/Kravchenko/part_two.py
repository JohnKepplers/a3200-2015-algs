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


def sorting(a, p, r):
    cr = []
    j = 0
    array = []
    for i in range(p, r + 1, 5):
        if r - p >= 4:
            array += insertion_sort([a[p + i], a[p + i + 1], a[p + i + 2], a[p + i + 3], a[p + i + 4]], 0, 5)
            j += 1
        else:
            while r - p > 0:
                cr += [a[i]]
                i += 1
            array += insertion_sort(cr, 0, len(cr))
    return array


def find_pivot(a, p, r):
    a = sorting(a, p, r)
    if r - p <= 4:
        if r - p == 4 or r - p == 3:
            return a[p + 2]
        elif r - p == 2 or r - p == 1:
            return a[p + 1]
        else:
            return a[p]
    array = []
    for i in range(p, r + 1, 5):
        if r - i >= 4:
            array += [a[i + 2]]
        else:
            if 1 < r - i < 4:
                array += [a[r - 1]]
            else:
                array += [a[r]]
    return find_pivot(array, 0, len(array) - 1)


def smart_partition(a, p, r):
    pivot = a.index(find_pivot(a, p, r))
    a[r], a[pivot] = a[pivot], a[r]
    x = a[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[r], a[i + 1] = a[i + 1], a[r]
    return i + 1


def select(a, p, r, i, const):
    ans = []
    if p == r:
        for i in range(p, p + const):
            ans += [a[i]]
        return ans
    q = smart_partition(a, p, r)
    n = q - p + 1
    if i == n:
        print(q)
        for i in range(q, q + const):
            ans += [a[i]]
        return ans
    elif i < n:
        return select(a, p, q - 1, i, const)
    else:
        return select(a, q + 1, r, i - n, const)


if __name__ == '__main__':
    k = int(stdin.readline())
    testing_array = [int(i) for i in stdin.readline().split()]
    const = k
    stdout.write(str(select(testing_array, 0, len(testing_array) - 1, len(testing_array) - k + 1, const)))

