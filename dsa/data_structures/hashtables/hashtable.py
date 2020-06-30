class HashTable(object):
    def __init__(self, length=4):
        self.array = [None] * length

    def hash(self, key):
        """takes in an arbitrary key and returns an index in the collection."""
        length = len(self.array)
        return hash(key) % length

    def add(self, key, value):
        """takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed."""
        index = self.hash(key)
        if self.array[index] is not None:
            for value in self.array[index]:
                if value[0] == key:
                    value[1] = value
                    break
            else:
                self.array[index].append([key, value])

        else:
            self.array[index] = []
            self.array[index].append([key, value])

    def get(self, key):
        """takes in the key and returns the value from the table."""
        index = self.hash(key)
        if self.array[index] is None:
            raise KeyError()
        else:
            for value in self.array[index]:
                if value[0] == key:
                    return value[1]

            raise KeyError()

    def contains(self, key):
        """ takes in the key and returns a boolean, indicating if the key exists in the table already."""
        index = self.hash(key)
        if key == index:
            print("exists")
        else:
            print("Sorry, it does not exist the the hashtable")
