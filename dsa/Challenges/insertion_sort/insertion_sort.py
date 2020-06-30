def insertion_sort(arr):
    for item in arr:
        j = item -1
        temp = arr[item]

        while j >= 0 and temp < item[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        arr[j + 1] = temp

