test_array = [1,2,3,4,5,6]

def binary_search(array, key):
	for element in range(len(array)):
		if array[element] == key:
			print(array[element])
		else:
			print(int(-1))

print(binary_search(test_array, 2))
