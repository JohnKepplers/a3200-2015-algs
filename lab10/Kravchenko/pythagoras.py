rom sys import stdin, stdout


def partition(ar):
    ar_odd = []
    ar_even = []
    helping_counter = 0
    for i in range(len(ar)):
        if ar[i] % 4 == 0:
            ar_even += [ar[i]]
        elif ar[i] % 2 == 1:
            ar_odd += [ar[i]]
            if ar[i] == 1:
                helping_counter += 1
    return search(ar_odd, ar_even, helping_counter)


def search(_ar_odd, _ar_even, counter):
    if len(_ar_odd) < 2:
        return 0
    if len(_ar_even) < 1:
        if counter < 3:
            return 0
        else:
            return 1
    the_great_counter = 0
    helping_counter = 0
    d = {}
    d.update({0: [-1, -1, -1]})
    for i in range(len(_ar_even)):
        for j in range(len(_ar_odd)):
            for k in range(len(_ar_odd)):
                if j != k:
                    if _ar_odd[i] == 1:
                        helping_counter += 1
                    if _ar_even[i] * _ar_even[i] + _ar_odd[j] * _ar_odd[j] == _ar_odd[k] * _ar_odd[k] and [
                                _ar_even[i] * _ar_even[i], _ar_odd[j] * _ar_odd[j], _ar_odd[k] * _ar_odd[k]] != d[
                        the_great_counter]:
                        the_great_counter += 1
                        d.update({the_great_counter: [_ar_even[i] * _ar_even[i], _ar_odd[j] * _ar_odd[j],
                                                      _ar_odd[k] * _ar_odd[k]]})
    if helping_counter < 3:
        return the_great_counter
    else:
        return the_great_counter + 1


if __name__ == '__main__':
    ar = [int(i) for i in stdin.readline().split()]
    stdout.write(str((partition(ar))))
