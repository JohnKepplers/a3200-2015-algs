rom sys import stdin, stdout


class MinHeap():
    def __init__(self):
        self.ar = []

    def print_array(self):
        return self.ar

    def size(self):
        return len(self.ar)

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
    a = [int(i) for i in stdin.readline().split()]
    testing_array = MinHeap()
    if len(a) >= k:
        for i in range(k):
            testing_array.insert(a[i])
        for i in range(k, len(a)):
            testing_array.insert(a[i])
            testing_array.extract_min()
        stdout.write(str(testing_array.print_array()))
    else:
        stdout.write('length is less than k. Error')
