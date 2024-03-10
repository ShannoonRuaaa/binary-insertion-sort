import numpy as np

# counter = 0


def binary_insertion_sort(array):
    # global counter
    sortedindex = 1
    while sortedindex + 1 < len(array):
        insertval = array[sortedindex + 1]
        insertindex = binary_search(array, 0, sortedindex, insertval)
        del array[sortedindex + 1]
        array.insert(insertindex, insertval)
        sortedindex += 1
        # counter += 1
    return array


def binary_search(array, left, right, value):
    # global counter
    if left > right:
        # counter += 1
        return left
    index = left + (right - left) // 2

    if array[index] == value:
        # counter += 1
        return index
    else:
        if array[index] > value:
            # counter += 1
            return binary_search(array, left, index - 1, value)
        else:
            # counter += 1
            return binary_search(array, index + 1, right, value)


arrr = [34, 55, 0, 1, 2, 5, 4, 87, 3, 1, 4, 5, 4, 7, 5, 5, 5]
print(binary_insertion_sort(arrr))
print((len(arrr)) * np.log2(len(arrr)))
# print(counter)
