__author__ = 'alexkane'


class Queue:
    def pop(self):
        pass

    def push(self, n):
        pass

    def size(self):
        pass


class StacksQueue(Queue):
    def __init__(self):
        self._stack1 = []
        self._stack2 = []
        self._direction = True

    def pop(self):
        if self._direction:
            for i in range(len(self._stack1) - 1):
                self._stack2.append(self._stack1.pop())
            value = self._stack1.pop()
            self._direction = False
            self._private_write(value)
        else:
            if len(self._stack2) != 0:
                value = self._stack2.pop()
                self._private_write(value)
            elif len(self._stack1) != 0:
                self._direction = True
                value = self.pop()
            else:
                value = "empty"
                print "empty"
        return value

    def _private_calc(self, n):
        print("push! " + str(n))

    def _private_write(self, n):
        print("pop! " + str(n))

    def _private_write_size(self, n):
        print("size! " + str(n))

    def push(self, n):
        self._stack1.append(n)
        self._private_calc(n)

    def size(self):
        self._private_write_size(len(self._stack1) + len(self._stack2))
        return len(self._stack1) + len(self._stack2)


class MaxElementQueue(Queue):
    def __init__(self):
        self._max = None
        self._queue = StacksQueue()
        self._tricky_list = []
        self._former_length = 0
        self._max_index = 0

    def pop(self):
        self._tricky_list = self._tricky_list[1:]
        if self._max_index < len(self._tricky_list):
            self._max = self._tricky_list[self._max_index]
        return self._queue.pop()

    def push(self, n):
        if self._max == None:
            self._max = n
            self._former_length += 1
        if n > self._max:
            self._max = n
            self._tricky_list = len(self._tricky_list) * [self._max]
            self._former_length = len(self._tricky_list)
        else:
            self._tricky_list.append(n)
            k = 1
            for i in range(len(self._tricky_list) - 2, self._former_length - 1, -1):
                if self._tricky_list[i] >= n:
                    break
                else:
                    k += 1
            if k != 1:
                self._tricky_list = self._tricky_list[:self._former_length] + k * [n]
        return self._queue.push(n)

    def size(self):
        return self._queue.size()

    def max(self):
        if self._max_index < len(self._tricky_list):
            return self._tricky_list[self._max_index]
        else:
            return "empty"
