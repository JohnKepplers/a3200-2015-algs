__author__ = 'alexkane'

from sys import stdin

if __name__ == "__main__":
    line = stdin.readline()
    input = [int(s) for s in line.split(" ")]

def execute(array):
    max = -float('inf')
    local_max = -float('inf')
    max_square = -float('inf')
    current_square = 0
    delta_x = 0
    delta_y = 0
    for i in range(len(array)):
        if array[i] >= max:
            max = array[i]
            if current_square > max_square:
                max_square = current_square
            current_square = 0
            delta_x = 0
            delta_y = 0
            local_max = -float('inf')
        elif i == len(array) - 1:
            if array[i] >= max:
                max = array[i]
                if current_square > max_square:
                    max_square = current_square
            else:
                if array[i] > local_max:
                    local_max = array[i]
                current_square += max - array[i]
                delta_x += 1
                delta_y = max - local_max
                current_square -= delta_x * delta_y
                if current_square > max_square:
                    max_square = current_square
        else:
            if array[i] > local_max:
                local_max = array[i]
            current_square += max - array[i]
            delta_x += 1
            delta_y = max - local_max
    return max_square

if __name__ == "__main__":
    print execute(input)


