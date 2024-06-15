def insertion_sort(arr):
    """
    Perform insertion sort on the given list.

    :param arr: List of numbers to be sorted
    :return: Sorted list
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
