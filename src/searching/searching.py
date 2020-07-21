# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if end >= start:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        else:
            return binary_search(arr, target, mid + 1, end)
    else:
        return -1


test_arr = [1]
print(binary_search(test_arr, 1, 0, len(test_arr) - 1))

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively


def agnostic_binary_search(arr, target, start=None, end=None):
    if start is None or end is None:
        start = 0
        end = len(arr) - 1
    # array is ascending
    if len(arr) == 1 or arr[0] < arr[1]:
        return binary_search(arr, target, 0, len(arr) - 1)
    # array is descending
    else:
        if end >= start:
            mid = (start + end) // 2
            print("start:", start, "end:", end, "mid:", mid)
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return agnostic_binary_search(arr, target, mid + 1, end)
            else:
                return agnostic_binary_search(arr, target, start, mid - 1)
        else:
            return -1


test_descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]
print(agnostic_binary_search(test_descending, 57))
