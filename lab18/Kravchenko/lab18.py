from sys import stdin, stdout


def distance(a, b):
    n, m = min(len(a), len(b)), max(len(a), len(b))
    if len(a) <= len(b):
        current_row = range(n + 1)
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change, transposition = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[
                    j - 1], max(previous_row[j] + 1, current_row[j - 1] + 1, previous_row[
                    j - 1])
                if a[j - 1] != b[i - 1]:
                    change += 1
                if a[j - 1] == b[i - 2]:
                    transposition = previous_row[j - 1]
                if a[j - 2] != b[i - 1]:
                    transposition += 1
                current_row[j] = min(add, delete, change, transposition)

        return current_row[n]
    else:
        current_row = range(n + 1)
        for i in range(1, m + 1):
            previous_row, current_row = current_row, [i] + [0] * n
            for j in range(1, n + 1):
                add, delete, change, transposition = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[
                    j - 1], max(previous_row[j] + 1, current_row[j - 1] + 1, previous_row[
                    j - 1])
                if b[j - 1] != a[i - 1]:
                    change += 1
                if b[j - 1] == a[i - 2]:
                    transposition = previous_row[j - 1]
                if b[j - 2] != a[i - 1]:
                    transposition += 1
                current_row[j] = min(add, delete, change, transposition)

        return current_row[n]


if __name__ == '__main__':
    a = stdin.readline()
    b = stdin.readline()
    stdout.write(str((distance(a, b))))

