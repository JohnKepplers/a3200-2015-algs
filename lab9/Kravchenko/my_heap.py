from sys import stdin, stdout


class MinHeap():
    def __init__(self):
        self.ar = []

    def size(self):
        return len(self.ar)
    def print_array(self):
        print(self.ar)

    def sift_down(self, i):
        while 2 * i + 1 < self.size():
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < self.size() and self.ar[right] < self.ar[left]:
                j = right
            if self.ar[i] < self.ar[j]:
                break
            self.ar[i], self.ar[j] = self.ar[j], self.ar[i]
            i = j

    def sift_up(self, i):
        while self.ar[i] < self.ar[int((i - 1) / 2)]:
            self.ar[i], self.ar[int((i - 1) / 2)] = self.ar[int((i - 1) / 2)], self.ar[i]
            i = int((i - 1) / 2)

    def extract_min(self):
        min = self.ar[0]
        self.ar[0] = self.ar[self.size() - 1]
        del self.ar[self.size() - 1]
        self.sift_down(0)
        return min

    def insert(self, element):
        self.ar.append(element)
        self.sift_up(self.size() - 1)


if __name__ == '__main__':
    k = int(stdin.readline())
    testing_array = MinHeap()
    for i in range(25):
        testing_array.insert(i)
    testing_array.insert(-64)
    testing_array.insert(13)
    n = testing_array.size() - k
    while n > 0:
        testing_array.extract_min()
        n-=1
    testing_array.print_array()
