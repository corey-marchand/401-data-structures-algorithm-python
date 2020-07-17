from dsa.challenges.pseudo_queue.pseudo_queue import PseudoQueue

def test_pseudoqueue_empty():
    test = PseudoQueue()
    actual = str(test)
    expected = "NULL"
    assert actual == expected


def test_dequeue():
    test = PseudoQueue()
    test.enqueue("food","chocolate")
    actual = test.dequeue()
    expected = "food"
    assert actual == expected


def test_enqueue():
    test = PseudoQueue()
    test.enqueue("food")
    expected = "food"
    assert actual == expected

