from sys import stdin
from random import randint

if __name__ == "__main__":
    line = stdin.readline()
    input = [int(s) for s in line.split(' ')]


def quick_sort(array, beginning_index, last_index):
    if beginning_index < last_index:
        new_ending_index, new_beginning_index = randomized_partition(array, beginning_index, last_index)
        quick_sort(array, beginning_index, new_ending_index)
        quick_sort(array, new_beginning_index + 1, last_index)


def partition(array, beginning_index, last_index):
    default_variable = array[last_index]
    i = beginning_index - 1
    k = beginning_index
    for j in range(beginning_index, last_index):
        if array[j] <= default_variable:
            i += 1
            array[i], array[j] = array[j], array[i]
            if array[i] == default_variable:
                array[i], array[k] = array[k], array[i]
                k += 1
    array[i + 1], array[last_index] = array[last_index], array[i + 1]
    j = i
    for x in range(beginning_index, k):
        array[j], array[x] = array[x], array[j]
        j -= 1
    return j, i + 1


def randomized_partition(array, beginning_index, last_index):
    i = randint(beginning_index, last_index)
    array[i], array[last_index] = array[last_index], array[i]
    return partition(array, beginning_index, last_index)


if __name__ == "__main__":
    quick_sort(input, 0, len(input) - 1)
    for x in input:
        print x,
