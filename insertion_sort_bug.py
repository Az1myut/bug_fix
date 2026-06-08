def insertion_sort(arr):
    """Sorts the list `arr` in ascending order using insertion sort.

    The original implementation had two bugs:
    1. The comparison in the inner loop was reversed (`arr[j] < key`),
       which caused the algorithm to shift elements in the wrong
       direction.
    2. The index ``j`` was incremented instead of decremented, so the
       algorithm would run forever for arrays that were already sorted
       in ascending order.

    Fixing both issues restores the classic insertion‑sort logic.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift elements that are greater than ``key`` to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage
numbers = [5, 2, 9, 1, 5, 6]

sorted_numbers = insertion_sort(numbers)

print("Sorted array:", sorted_numbers)
