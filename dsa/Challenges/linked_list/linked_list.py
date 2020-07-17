class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_Node = Node(data)
        if(self.head):
            current = self.head
            while(current.ref):
                current = current.ref
            current.ref = new_Node
        else:
            self.head = new_Node

    def includes(self,x):
        current = self.head

        while current != None:
            if current.data == x:
                return True
            current = current.ref
        return False

    def _str_(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.ref

    def append(value)
	    node = Node(value)
	    if self.head:
		    self.head.next == node
		    self.head == node
	    else:
		    self.tail equals node
		    self.head equals node

    def insertBefore(val, newVal):
	    new_node = Node(val)
	    node = self.head
	    if node != None:
		    print(‘does not exist’)
	    else:
		    found = None
		    while node:
			    if node.next.value == val:
				    Found == true
				    print node.value(val)


    def insertAfter(val, newVal):
        node = Node(val)
        new_node = Node(newVal)
        temp == self.head
        while temp:
            if temp.value == node:
                new_node.next = node.next
                node.next = new_node
            Temp = temp.next


if __name__=='__main__':
    ll = LinkedList()
    ll.insert(5)
    ll.insert(14)
    ll.insert(15)
    ll.insert(13)
    ll.insert(4)
    ll._str_()
    if ll.includes(13):
        print("yes")
    else:
        print("no")
