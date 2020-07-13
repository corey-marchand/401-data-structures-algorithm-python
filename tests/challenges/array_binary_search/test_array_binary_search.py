from dsa.challenges.array_binary_search.array_binary_search import binary_search

def test_one():
    test_array = [1,2,3,4,5]
    actual = binary_search(test_array, 3)
    expected = [-1,-1,2,-1,-1]
    assert actual == expected
