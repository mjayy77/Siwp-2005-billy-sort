def bubble_sort(arr):
    """
    Perform bubble sort on the given list.

    :param arr: List of numbers to be sorted
    :return: Sorted list
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
