from sys import stdin, stdout


def partition(ar):
    ar_odd = []
    ar_even = []
    for i in range(len(ar)):
        if ar[i] % 4 == 0:
            ar_even += [ar[i]]
        elif ar[i] % 2 == 1:
            ar_odd += [ar[i]]
    return search(ar_odd, ar_even)


def search(_ar_odd, _ar_even):
    if len(_ar_odd) < 2:
        return 0
    if len(_ar_even) < 1:
        return 0
    the_great_counter = 0
    d = {}
    u = 0
    d.update({0: [-1, -1, -1]})
    for i in range(len(_ar_even)):
        for j in range(len(_ar_odd)):
            for k in range(len(_ar_odd)):
                if j != k:
                    if _ar_even[i] * _ar_even[i] + _ar_odd[j] * _ar_odd[j] == _ar_odd[k] * _ar_odd[k]:
                        for h in range(0, the_great_counter + 1):
                            if [_ar_even[i] * _ar_even[i], _ar_odd[j] * _ar_odd[j], _ar_odd[k] * _ar_odd[k]] == d[h]:
                                u = 1
                                break
                        if u == 0:
                            the_great_counter += 1
                            d.update({the_great_counter: [_ar_even[i] * _ar_even[i], _ar_odd[j] * _ar_odd[j],
                                                          _ar_odd[k] * _ar_odd[k]]})
                            print(d[the_great_counter])
                        else:
                            u = 0
    return the_great_counter


if __name__ == '__main__':
    ar = [int(i) for i in stdin.readline().split()]
    stdout.write(str((partition(ar))))
