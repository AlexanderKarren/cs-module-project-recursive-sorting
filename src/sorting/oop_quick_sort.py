# out of place quicksort

def partition(data):
    left = []
    right = []
    pivot = data[0]

    for i in range(1, len(data)):
        if data[i] > pivot:
            right.append(data[i])
        else:
            left.append(data[i])

    return left, right, pivot


def quicksort(data):
    # check if data has 1 or 0 elements
    # (base case) a side only contains a single element
    if len(data) <= 1:
        return data

    left, right, pivot = partition(data)

    # (recursive case) Recursively quick sort LHS and RHS until
    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([2, 5, 7, 1, 3, 4, 6, 9, 8]))
