from sys import stdin, stdout

testing_array = [int(i) for i in stdin.readline().split()]


def search(ar):
    max_s = 0
    s = 0
    maximum = ar[0]
    for i in range(1, len(ar)):
        if ar[i] < maximum:
            s += maximum - ar[i]
        else:
            if s > max_s:
                max_s = s
            s = 0
            maximum = ar[i]
    return max_s


if __name__ == '__main__':
    stdout.write(str(search(testing_array)))

