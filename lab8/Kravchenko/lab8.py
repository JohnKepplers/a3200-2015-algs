class Queue:
    def pop(self):
        pass

    def push(self, n):
        pass

    def size(self):
        pass


class StacksQueueWithMaxElement(Queue):
    def __init__(self):
        self.pop_stack = []
        self.push_stack = []
        self.max_push_stack = []
        self.max_pop_stack = []

    def push(self, n):
        self.push_stack.append(n)
        if len(self.max_push_stack) == 0:
            self.max_push_stack.append(n)
        else:
            if n > self.max_push_stack[len(self.max_push_stack) - 1]:
                self.max_push_stack.append(n)
            else:
                self.max_push_stack.append(self.max_push_stack[len(self.max_push_stack) - 1])
        return 'ok'

    def pop(self):
        k = 0
        if len(self.pop_stack) == 0:
            if len(self.push_stack) == 0:
                return 'empty'
            else:
                self.pop_stack = self.push_stack[1:-1]
                k = self.push_stack[0]
                self.push_stack.clear()
                self.max_push_stack.clear()
                self.max_pop_stack.append(self.pop_stack[0])
                for i in range(len(self.pop_stack), 1, -1):
                    if len(self.max_pop_stack) == 0:
                        self.max_pop_stack.append(self.pop_stack[i])
                    else:
                        if self.pop_stack[i] > self.max_pop_stack[len(self.pop_stack) - i]:
                            self.max_pop_stack.append(self.pop_stack[i])
                        else:
                            self.max_pop_stack.append(self.max_pop_stack[len(self.pop_stack) - i])
        return k

    def size(self):
        return len(self.push_stack) + len(self.pop_stack)

    def max(self):
        if len(self.max_push_stack) == 0 and len(self.max_pop_stack) == 0:
            return 'empty'
        elif len(self.max_push_stack) != 0 and len(self.max_pop_stack) == 0:
            return self.max_push_stack[len(self.max_push_stack) - 1]
        elif len(self.max_push_stack) == 0 and len(self.max_pop_stack) != 0:
            return self.max_pop_stack[len(self.max_pop_stack) - 1]
        else:
            return max(self.max_push_stack[len(self.max_push_stack) - 1], self.max_pop_stack[len(self.max_pop_stack) - 1])


if __name__ == '__main__':
    queue = StacksQueueWithMaxElement()
    c = [str(i) for i in input().split()]
    while c:
        command = c[0]
        if command == 'push':
            print(queue.push(int(c[1])))
        elif command == 'pop':
            print(queue.pop())
        elif command == 'size':
            print(queue.size())
        elif command == 'max':
            print(queue.max())
        else:
            print('Error!')
        c = [str(i) for i in input().split()]
