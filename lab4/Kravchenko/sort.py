import sys
from sys import stdin, stdout

first_line = stdin.readline()
a = [int(j) for j in first_line.split()]
res = [0 for j in range(len(a))]


def insertion_sort(ar):
    for j in range(1, len(ar)):
        key = ar[j]
        i = j - 1
        while (i >= 0) and (ar[i] > key):
            ar[i + 1] = ar[i]
            i -= 1
        ar[i + 1] = key


def merge_sort(a, p, r, k):
    if r - p <= k:
        insertion_sort(a)
    elif p < r:
        q = int((p + r) / 2)
        merge_sort(a, p, q, k)
        merge_sort(a, q + 1, r, k)
        merge(a, p, q, r)


def merge(a, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = [0 for x in range(n1 + 1)]
    right = [0 for y in range(n2 + 1)]
    for i in range(n1):
        left[i] = a[p + i]
    for j in range(n2):
        right[j] = a[q + j + 1]
    left[n1] = sys.maxsize
    right[n2] = sys.maxsize
    i = 0
    j = 0
    for l in range(p, r + 1):
        if left[i] <= right[j]:
            a[l] = left[i]
            i += 1
        else:
            a[l] = right[j]
            j += 1


merge_sort(a, 0, len(a) - 1, 10)
print(a)
