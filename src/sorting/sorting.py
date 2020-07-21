# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i = j = k = 0

    # compare lists and add to merged_arr accordingly
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1

    # account for leftover numbers (unequal list lengths)
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    print("merge:", arrA, arrB, merged_arr)

    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    return merge(left, right)


test_arr = [2, 8, 5, 3, 9, 4, 1, 7]
# print(merge_sort(test_arr))
merge_sort(test_arr)

# test_arr_1 = [2]
# test_arr_2 = [8]
# test_arr_3 = [3]
# test_arr_4 = [5]

# print(merge(test_arr_1, test_arr_2))
# print(merge(test_arr_3, test_arr_4))

# print(merge(merge(test_arr_1, test_arr_2), merge(test_arr_3, test_arr_4)))

# print(merge([2, 8], [3, 5]))


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, left, right):
    pass
