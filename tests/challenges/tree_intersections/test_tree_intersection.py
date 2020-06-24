from dsa.challenges.tree_intersection.tree_intersection import tree_intersection

def test_one():
    actual = tree_intersection([1,3,2,1,4],[1,6,88,6,4])
    expected = 1,4
    assert actual == expected

