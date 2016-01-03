from sys import stdin, stdout


def palindrome(string):
    matrix = [[0 for i in range(len(string) - 1)] for j in range(len(string) - 1)]
    helping_matrix = [[0 for i in range(len(string) - 1)] for j in range(len(string) - 1)]
    res1 = ""
    res2 = ""
    res3 = ""
    for i in range(len(string) - 1, -1, -1):
        for j in range(i, len(string) - 1):
            if i == j:
                matrix[i][j] = 1
            elif string[i] == string[j]:
                matrix[i][j] = matrix[i + 1][j - 1] + 2
                helping_matrix[i][j] = 3

            else:
                matrix[i][j] = max(matrix[i + 1][j], matrix[i][j - 1])
                if matrix[i + 1][j] > matrix[i][j - 1]:
                    helping_matrix[i][j] = 1
                else:
                    helping_matrix[i][j] = 2
    i = 0
    j = len(helping_matrix) - 1
    while i < j:
        if helping_matrix[i][j] == 3:
            res1 += string[j]
            res3 += string[j]
            i += 1
            j -= 1
            if i == j == (len(string) - 1) // 2:
                res2 = string[i]
            continue
        if helping_matrix[i][j] == 1:
            i += 1
            continue
        if helping_matrix[i][j] == 2:
            j -= 1
            continue
    ans = res1 + res2 + res3[::-1]
    if ans == "":
        ans = string[0]
    return ans


if __name__ == '__main__':
    my_string = stdin.readline()
    stdout.write(str((palindrome(my_string))))
