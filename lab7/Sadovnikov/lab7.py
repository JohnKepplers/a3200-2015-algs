# coding=utf-8
from random import randint
import time

__author__ = 'alexkane'

import matplotlib.pyplot as plt
import lab4
import lab5
import lab6

funcs = 4 * [None]
funcs[0] = lambda x: x.sort()
funcs[1] = lambda x: lab4.sort(x)
funcs[2] = lambda x: lab5.quick_sort(x, 0, len(x) - 1)
funcs[3] = lambda x: lab6.radix_sort(x)

array_of_names =  4 * [None]
array_of_names[0] = "Basic"
array_of_names[1] = "Merge/insert"
array_of_names[2] = "Quick"
array_of_names[3] = "Radix"


def universal_plot(fig, ax, term):
    xrng = xrange(100, 1000000, 100000)
    t = 0
    for func in funcs:
        array_of_medians = 10 * [None]
        m = 0
        for k in xrng:
            if term == 0:
                array = [randint(-1000000, 1000000) for x in range(k)]
            elif term == 1:
                array = [randint(0, 10000) for x in range(k)]
            elif term == 2:
                array = []
                counter = k
                while counter > 0:
                    len = randint(0, counter)
                    addition = randint(0, 9900)
                    sub_array = [x + addition for x in range(len)]
                    array += sub_array
                    counter -= len
                    len = randint(0, counter)
                    addition = randint(0, 9900)
                    sub_array = [len - 1 - x + addition for x in range(len)]
                    array += sub_array
                    counter -= len
            elif term == 3:
                array = [x for x in range(k)]
                array.sort()
            elif term == 4:
                array = [x for x in range(k)]
                array.reverse()
            else:
                const = randint(0, 10000)
                array = [const for x in range(k)]
            array_of_time = 5 * [None]
            print "getting median"
            for i in range(5):
                beginning = time.time()
                func(array)
                array_of_time[i] = time.time() - beginning
            array_of_time.sort()
            array_of_medians[m] = array_of_time[2]
            m += 1
        ax.plot(xrng, array_of_medians, label=array_of_names[t])
        t += 1
    ax.set_xlabel('size', fontsize=8)
    ax.set_ylabel('ms', fontsize=8)
    ax.set_title('plot name', fontsize=8)


fig = plt.figure()
term = 0
for i in range(2):
    for j in xrange(3):
        ax = plt.subplot2grid((2, 3), (i, j))
        universal_plot(fig, ax, term)
        term += 1

plt.legend(loc='upper left', title="funcs")
plt.tight_layout()
plt.show()
