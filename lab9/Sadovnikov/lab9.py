from sys import stdin

if __name__ == "__main__":
    the_k = int(stdin.readline())
    line = stdin.readline()
    input = [int(s) for s in line.split(' ')]


class HeapPriorityQueue:
    def __init__(self):
        self._number_of_max = 0
        self._array = []
        self._successful = False

    def insert(self, key):
        if len(self._array) < self._number_of_max:
            self._array.append((-1) * float('inf'))
            self.increase_key(len(self._array) - 1, key)
        else:
            min = float('inf')
            x = 0
            for i in range(len(self._array) - 1, len(self._array) / 2 - 1, -1):
                if self._array[i] < min:
                    min = self._array[i]
                    x = i
            self.increase_key(x, key)

    def max(self):
        return self._array[0]

    def extract_max(self):
        if len(self._array) == 0:
            print "empty"
        max = self._array[0]
        self._array[0], self._array[len(self._array) - 1] = self._array[len(self._array) - 1], self._array[0]
        self._array = self._array[:len(self._array) - 1]
        self._max_heapify(self._array, 0)
        return max

    def increase_key(self, i, key):
        if key > self._array[i]:
            self._successful = True
            self._array[i] = key
            while i > 0 and self._array[i / 2] < self._array[i]:
                self._array[i], self._array[i / 2] = self._array[i / 2], self._array[i]
                i /= 2

    def _max_heapify(self, array, i):
        l = i * 2
        r = i * 2 + 1
        if l < len(array) and array[l] < array[i]:
            largest = l
        else:
            largest = i
        if r < len(array) and array[r] > array[largest]:
            largest = r
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            self._max_heapify(array, largest)

    def set_special_k(self, k):
        self._number_of_max = k

    def get_array(self):
        for i in range(len(self._array)):
            print self._array[i],
        return self._array


if __name__ == "__main__":
    heap = HeapPriorityQueue()
    heap.set_special_k(the_k)

    for i in range(len(input)):
        heap.insert(input[i])

    heap.get_array()
