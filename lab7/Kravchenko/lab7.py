import merge_sort
import q_sort
import radix_sort
import lists
from random import randint
from time import time
import pylab

lists = {"Random numbers in [-1.000.000, 1.000.000]": lists.positive_and_negative_random_list,
         "Random numbers in [0, 10.000]": lists.positive_random_list,
         "Partially sorted numbers in [0, 10.000]": lists.strange_sorted_list,
         "Ascending sorted numbers in  [0, 10.000]": lists.normal_sort_list,
         "Descending sorted numbers in  [0, 10.000]": lists.abnormal_sort_list,
         "Same numbers": lists.boring_list
         }

functions = {"Merge sort": merge_sort,
             "Quick sort": q_sort,
             "Radix sort": radix_sort,
             "Enemy sort": sorted}
number_of_subwindow = 1
mne_nujny_bally = [100 + 100000 * bally for bally in range(5)]
for list_name, lists in lists.items():
    pylab.subplot(2, 3, number_of_subwindow)
    pylab.xlabel("size, elem")
    pylab.ylabel("time, sec")
    print("On the battlefield: ", list_name)
    for func_name, func in functions.items():
        millis = []
        for size in mne_nujny_bally:
            spaggiari = 0.0
            for bally in range(5):
                array = lists(size)
                t1 = time()
                func(array)
                t2 = time()
                spaggiari += t2 - t1
            spaggiari /= 5.0
            millis += [spaggiari]
            print("Using ", func_name, " on list of size ", size)
        pylab.plot(mne_nujny_bally, millis, label=func_name)
    pylab.title(list_name)
    pylab.legend(loc='upper left', title="Sorts")
    number_of_subwindow += 1

pylab.show()
