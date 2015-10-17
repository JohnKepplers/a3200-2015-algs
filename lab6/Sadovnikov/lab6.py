from sys import stdin


line = stdin.readline()
input = [int(s) for s in line.split(' ')]


def stable_sort(input, index, k):
    if index > 0:
        array = [(input[i] / (10 ** index)) % 10 for i in range(len(input))]
    else:
        array = [input[i] % 10 for i in range(len(input))]
    c = (k + 1) * [0]
    output = len(input) * [0]
    for i in range(len(input)):
        c[array[i]] += 1
    for i in range(1, k + 1):
        c[i] += c[i - 1]
    for j in range(len(input) - 1, -1, -1):
        c[array[j]] -= 1
        output[c[array[j]]] = input[j]
    for i in range(len(input)):
        input[i] = output[i]


def radix_sort(input):
    d = 0
    positive = []
    negative = []
    for i in range (len(input)):
        if input[i] >= 0:
            positive.append(input[i])
        else:
            negative.append(input[i])
    for x in range(len(positive)):
        while positive[x] / (10 ** d) != 0:
            d += 1
    for i in range(0, d):
        stable_sort(positive, i, 9)
    d = 0
    for x in range(len(negative)):
        while negative[x] / -(10 ** d) != 0:
            d += 1
    for i in range(0, d):
        stable_sort(negative, i, 9)
    input = negative + positive
    for x in range(len(input)):
    print input[x],

radix_sort(input)


