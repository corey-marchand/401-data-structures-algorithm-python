class PseudoQueue:
    def __init__(self):
        self.enqueue = Stack()
        self.dequeue = Stack()

    def enqueue(self, new_val, *args):
        while not self.dequeue.isEmpty():
            self.enqueue.push(self.dequeue.pop())
        self.enqueue.push(new_val, *args)
        return

    def dequeue(self):
        while not self.enqueue.isEmpty():
            self.dequeue.push(self.enqueue.pop())

        if self.dequeue.isEmpty():
            raise RuntimeError("cannot dequeue from empty queue")

        return self.dequeue.pop()
