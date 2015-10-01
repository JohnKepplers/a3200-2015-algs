import sys


def sort(a):
    if len(a) < 10:
        insert_sort(a, 0, len(a))
    else:
        merge_sort(a, 0, len(a) - 1)


def insert_sort(a, p, q):
    for j in range(p, q):
        key = a[j]
        i = j - 1
        while i >= p and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key


def merge_sort(a, p, r):
    if r - p < 10:
        insert_sort(a, p, r)
    else:
        q = (p + r) / 2
        if (q - p) >= 10:
            merge_sort(a, p, q)
        else:
            insert_sort(a, p, q + 1)
        if (r - q - 1) >= 10:
            merge_sort(a, q + 1, r)
        else:
            insert_sort(a, q + 1, r + 1)
        merge(a, p, q, r)


def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left_array = [None] * (n1 + 1)
    right_array = [None] * (n2 + 1)
    for i in range(n1):
        left_array[i] = a[p + i]
    for i in range(n2):
        right_array[i] = a[q + i + 1]
    left_array[n1] = sys.maxint
    right_array[n2] = sys.maxint
    i = 0
    j = 0
    for k in range(p, r + 1):
        if left_array[i] <= right_array[j]:
            a[k] = left_array[i]
            i += 1
        else:
            a[k] = right_array[j]
            j += 1
