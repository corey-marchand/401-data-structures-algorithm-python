from dsa.data_structures.hashtables.hashtable import HashTable

def test_Hashtable_empty():
    actual = HashTable(10)
    expected = None
    assert actual == expected

def test_Hashtable_hash():
    test_hash = HashTable(10)
    actual = test_hash.hash("test")
    expected = 1
    assert actual == expected

def test_HashTable_add():
    test_hash = HashTable(10)
    test_hash.add("my",30)
    actual = str(test_hash)
    expected = str(["my", 30])
    assert actual == expected

def test_HashTable_get():
    test_hash = HashTable(10)
    test_hash.add('my', 45)
    actual = str(test_hash.get('my'))
    expected = str(45)
    assert actual == expected

def test_HashTable_contains():
    test_hash = HashTable(10)
    test_hash.add('my', 45)
    actual = test_hash.contains('my')
    expected = True
    assert actual == expected

def test_HashTable_collision():
    test_hash = HashTable(10)
    test_hash.add('tee', 45)
    test_hash.add('eet', 25)
    actual = test_hash.contains('tee')
    expected = True
    assert actual == expected

def test_HashTable_collision_get():
    test_hash = HashTable(10)
    test_hash.add('foo', 25)
    actual = str(test_hash.get("foo"))
    expected = str(25)
    assert actual == expected
