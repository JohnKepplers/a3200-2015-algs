__author__ = 'alexkane'

from sys import stdin

if __name__ == "__main__":
    first_line = stdin.readline().rstrip('\n')
    second_line = stdin.readline().rstrip('\n')

def execute(line_a, line_b):
    line_one = [float('inf') for i in range(len(line_a))]
    line_two = [float('inf') for i in range(len(line_a))]

    for i in range(len(line_b)):
        for j in range(len(line_a)):
            if i == j == 0:
                if line_a[0] == line_b[0]:
                    line_one[0] = 0
                else:
                    line_one[0] = 1
            else:
                if i % 2 == 0:
                    current_line = line_one
                    previous_line = line_two
                else:
                    current_line = line_two
                    previous_line = line_one
                val = min(previous_line[j - 1] + int(not(line_b[i] == line_a[j])), previous_line[j] + 1, current_line[j - 1] + 1, previous_line[j - 1] + int(not((line_b[i - 1] == line_a[j]) and (line_b[i] == line_a[j - 1]))))
                if i % 2 == 0:
                    line_one[j] = val
                else:
                    line_two[j] = val
    if len(line_a) == len(line_b) == 1:
        return 1
    else:
        return line_two[len(line_a) - 1]

if __name__ == "__main__":
    print(execute(first_line, second_line))

