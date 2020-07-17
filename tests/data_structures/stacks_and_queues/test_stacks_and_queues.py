import pytest

from dsa.data_structures.stacks_and_queues.stacks_and_queues import Node, Stack, Queue, QueueDeque

def test_Stack_instantiate_empty_stack():
    test = Stack()
    actual = str(test)
    expected = "NULL"
    assert actual == expected

def test_stack_new_val():
    test = Stack()
    test.push("candy")
    actual = str(fruit)
    expected = "candy"
    assert actual == expected

def test_Stack_pop(test):
    actual = test.pop()
    expected = "candy"
    assert actual == expected

def test_Stack_push_multipleValues(test):
    test.push("1","2","3")
    actual = test
    expected = ("1","2","3")
    assert actual == expected

def test_empty_queue():
    queue = Queue()
    actual = queue.isEmpty()
    expected = True
    assert actual == expected

