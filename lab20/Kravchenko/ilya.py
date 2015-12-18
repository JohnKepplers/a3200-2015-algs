from sys import stdin, stdout


def rectangular(n, array):
    if n <= 3:
        return 0
    answer = 0
    i = n - 2
    crutch = 0
    array.sort()
    while i >= 0:
        if array[i + 1] - array[i] <= 1:
            if crutch == 0:
                crutch = array[i]
                i -= 1
            else:
                answer += crutch * array[i]
                crutch = 0
                i -= 1
        i -= 1
    return answer


if __name__ == "__main__":
    n = int(stdin.readline())
    array = [int(i) for i in stdin.readline().split()]
    stdout.write(str(rectangular(n, array)))
