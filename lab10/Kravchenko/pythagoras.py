from sys import stdin, stdout


def pythagoras(array):
    helping_array = []
    for i in range(len(array)):
        helping_array.append(array[i] * array[i])
    counter = 0
    helping_array.sort()
    j = 0
    a = len(helping_array)
    while j < a:
        true_square = helping_array[j]
        i = j + 1
        while i < a and true_square == helping_array[i]:
            del helping_array[i]
            a -= 1
        j += 1
    for i in range(2, a):
        left = 0
        right = i - 1
        while left < right:
            if helping_array[left] + helping_array[right] == helping_array[i]:
                counter += 1
            if helping_array[left] + helping_array[right] < helping_array[i]:
                left += 1
            else:
                right -= 1
    return counter


if __name__ == '__main__':
    ar = [int(i) for i in stdin.readline().split()]
    stdout.write(str(pythagoras(ar)))

