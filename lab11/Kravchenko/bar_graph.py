from sys import stdin, stdout


def search(ar):
    maximum = 0
    max_s = 0
    s = 0
    if len(ar) != 0:
        maximum = ar[0]
    for i in range(1, len(ar)):
        if ar[i] < maximum:
            s += maximum - ar[i]
        else:
            if s > max_s:
                max_s = s
            s = 0
            maximum = ar[i]
    s = 0
    maximum = ar[len(ar) - 1]
    for i in range(len(ar) - 2, -1, -1):
        if ar[i] < maximum:
            s += maximum - ar[i]
        else:
            if s > max_s:
                max_s = s
            s = 0
            maximum = ar[i]
    return max_s


if __name__ == '__main__':
    testing_array = [int(i) for i in stdin.readline().split()]
    stdout.write(str(search(testing_array)))
