from sys import stdin

if __name__ == "__main__":
    the_k = int(stdin.readline())
    line = stdin.readline()
    input = [int(s) for s in line.split(' ')]


class HeapPriorityQueue:
    def __init__(self):
        self._number_of_max = 0
        self._array = []

    def insert(self, key):
        if len(self._array) < self._number_of_max:
            self._array.append((-1) * float('inf'))
            self.increase_key(len(self._array) - 1, key)
        else:
            self.increase_key(0, key)
            self._min_heapify(self._array, 0)

    def increase_key(self, i, key):
        if key > self._array[i]:
            self._array[i] = key
            while i > 0 and self._array[i / 2] > self._array[i]:
                self._array[i], self._array[i / 2] = self._array[i / 2], self._array[i]
                i /= 2

    def _min_heapify(self, array, i):
        l = i * 2
        r = i * 2 + 1
        if l < len(array) and array[l] < array[i]:
            smallest = l
        else:
            smallest = i
        if r < len(array) and array[r] < array[smallest]:
            smallest = r
        if smallest != i:
            array[i], array[smallest] = array[smallest], array[i]
            self._min_heapify(array, smallest)

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
