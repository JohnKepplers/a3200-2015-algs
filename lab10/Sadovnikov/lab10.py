import math
from sys import stdin

__author__ = 'alexkane'

if __name__ == "__main__":
    line = stdin.readline()
    input = [int(s) for s in line.split(' ')]


def execute_search(array):
    n = len(array)
    new_array = []
    wicked_array = []
    counter = 0
    for i in range(n):
        for j in range(i + 1, n):
            x = math.sqrt(array[i] ** 2 + array[j] ** 2)
            if x % 1 == 0:
                new_array.append(int(x))
                wicked_array.append(array[j])
    wicked_array.sort()
    for i in range(len(wicked_array)):
        if wicked_array[i] != wicked_array[i - 1]:
            for j in range(i + 1, len(wicked_array)):
                if wicked_array[i] == wicked_array[j]:
                    counter -= 1
    for i in range(len(new_array)):
        for j in range(n):
            if new_array[i] == array[j]:
                counter += 1
                break
    return counter

if __name__ == "__main__":
    print execute_search(input)

# 18 100 99 24 40 10 10 24 4 30 3 5 1 88 24 32 32 26