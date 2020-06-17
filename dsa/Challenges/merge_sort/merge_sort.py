def merge_sort(list_ex):
    if len(list_ex) > 1:
        mid = len(list_ex) // 2
        left = list_ex[:mid]
        right = list_ex[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list_ex[k] = left[i]
                i += 1

            else:
                list_ex[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            list_ex[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list_ex[k] = right[j]
            j += 1
            k += 1


list_ex = [8,4,23,42,16,15]
print(merge_sort([]))
