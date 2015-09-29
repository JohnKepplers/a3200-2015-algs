def insertion_sort(a, p, r):
    for j in range(p, r):
        key = a[j]
        i = j - 1
        while i >= p and a[i] > key:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = key


def merge_sort(a, p, r, k):
    if r - p <= k:
        insertion_sort(a, p, r)
    else:
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
    left[n1] = maxsize
    right[n2] = maxsize
    i = 0
    j = 0
    for l in range(p, r + 1):
        if left[i] <= right[j]:
            a[l] = left[i]
            i += 1
        else:
            a[l] = right[j]
            j += 1
