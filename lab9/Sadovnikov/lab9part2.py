__author__ = 'alexkane'

from sys import stdin



if __name__ == "__main__":
    special_k = int(stdin.readline())
    line = stdin.readline()
    input = [int(s) for s in line.split(' ')]


def quick_search(array, beginning_index, last_index):
    if beginning_index < last_index:
        new_index = find_pivot(array, beginning_index, last_index)
        quick_search(array, new_index + 1, last_index)
        quick_search(array, beginning_index, new_index)
    return array

def find_pivot(array, beginning_index, last_index):
    array_counter = 0
    if last_index - beginning_index < 5:
        n = last_index - beginning_index
    else:
        n = 5
    local_array = []
    array_of_medians = []
    for k in range(beginning_index, last_index):
        if array_counter < n - 1:
            local_array.append(array[k])
            array_counter += 1
        else:
            local_array.append(array[k])
            array_counter = 0
            for j in range(0, n):
                key = local_array[j]
                i = j - 1
                while i >= 0 and local_array[i] > key:
                    local_array[i + 1] = local_array[i]
                    i -= 1
                local_array[i + 1] = key
            if last_index - k < n:
                n = last_index - k - 1
            array_of_medians.append(local_array[len(local_array) / 2])
            local_array = []
    array_of_medians.sort()
    the_median = array_of_medians[len(array_of_medians) / 2]
    array[array.index(the_median)], array[last_index - 1] = array[last_index - 1], array[array.index(the_median)]
    return partition(array, beginning_index, last_index - 1)


def partition(array, beginning_index, last_index):
    default_variable = array[last_index]
    i = beginning_index - 1
    for j in range(beginning_index, last_index):
        if array[j] <= default_variable:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[last_index] = array[last_index], array[i + 1]
    return i + 1


if __name__ == "__main__":
    quick_search(input, 0, len(input))
    for x in range(len(input) - special_k, len(input)):
        print input[x],
