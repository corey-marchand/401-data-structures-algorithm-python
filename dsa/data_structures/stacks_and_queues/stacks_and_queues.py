from collections import deque

class Node:
    def __init__ (self, value, next_ = None):
        self.value = value
        self.next = next_

    def __str__(self):
        return f"{self.value} : {self.next}"

    def __repr__(self):
        return f"{self.value} : {self.next}"

class Stack:
    def __init__(self):
        self.top = None

    def push(self, new_value, *args):
        if self.isEmpty():
            self.top = Node(new_value)
        else:
            self.top = Node(new_value, self.top)
        if len(args):
            curr = self.top
            for arg in args:
                node = Node(arg, curr)
                curr = node
            self.top = curr
        return

    def pop(self):
        if self.isEmpty():
            raise Exception("this is an empty stack")
        curr = self.top
        if curr.next:
            newVal = curr.next
            curr.next = None
            self.top = newVal
        else:
            self.top = None
        return curr.value

    def isEmpty(self):
        if not self.top:
            return True
        return False

    def peek(self):
        if self.isEmpty():
            raise Exception("sorry the stack is empty")
        return self.top.value

    def __str__(self):
        final_string = ""
        curr = self.top

        while curr:
            final_string += f"{{{curr.value}}} -> "
            curr = curr.next

        return f"{final_string}NULL"

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, new_value):
        if self.isEmpty():
            self.rear = Node(new_value)
            self.front = self.rear
            return
        curr = self.rear
        curr.next = Node(new_value)
        self.rear = curr.next
        return

    def dequeue(self):
        if not self.front:
            print('empty')
        curr = self.front
        if curr.next:
            self.front = curr.next
            curr.next = None
        else:
            self.front = None
            self.rear = None
        return curr.value

    def peek(self):
        if self.isEmpty():
            print('empty')
        return self.front.value

    def isEmpty(self):
        if not self.front:
            return True
        return False

    def __str__(self):
        final_string = ""
        curr = self.front

        while curr:
            final_string += f"{{{curr.value}}}"
            curr = curr.next

        return f"{final_string}"

class QueueDeque():
    def __init__(self):
        self.storage = deque()
    def enqueue(self,new_value):
        if len(self.storage):
            node = Node(new_value, self.storage[0])
            print("this is in self.storage", self.storage)
            self.storage.appendleft(node)
        else:
            self.storage.appendleft(Node(new_value))
        return
    def dequeue(self):
        return self.storage.pop()
    def peek(self):
        return self.storage[-1]
    def is_empty(self):
        return len(self.storage)==0
    def __str__(self):
        final_string = ""
        for item in self.storage:
            final_string += f"{{{str(item.value)}}}"
        return f"{final_string}"
