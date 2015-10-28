from sys import stdin, stdout

testing_array = [int(i) for i in stdin.readline().split()]


def search(ar):
    a = []
    max_s = 0
    s = 0
    a += [ar[0]]
    for i in range(1, len(ar)):
        if ar[i] < a[0]:
            a += [ar[i]]
        else:
            for j in range(1, len(a)):
                s += a[0] - a[j]
            a = [ar[i]]
            if s > max_s:
                max_s = s
            s = 0
    return max_s


if __name__ == '__main__':
    stdout.write(str(search(testing_array)))
