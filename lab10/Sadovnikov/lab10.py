import math
from sys import stdin

__author__ = 'alexkane'

if __name__ == "__main__":
    line = stdin.readline()
    input = [int(s) for s in line.split(' ')]


def execute_search(array):
    n = len(array)
    counter = 0
    for i in range(n):
        array[i] **= 2
    array.sort()
    for i in range(n - 1):
        j = i
        k = 0
        while True:
            if j == k or j < k:
                break
            if array[k] + array[j] == array[i]:
                counter += 1
                j -= 1
                while array[j] == array[j + 1]:
                    j -= 1
                k += 1
                while array[k - 1] == array[k]:
                    k += 1
            elif array[k] + array[j] > array[i]:
                j -= 1
            else:
                k += 1
    return counter


if __name__ == "__main__":
    print(execute_search(input))

    # 18 100 99 24 40 10 10 24 4 30 3 5 1 88 24 32 32 26
