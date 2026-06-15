def insertion_sort(arr):
    # Handle edge cases for empty or single-element arrays
    if len(arr) <= 1:
        return arr
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

numbers = [5, 2, 9, 1, 5, 6]

sorted_numbers = insertion_sort(numbers)

print("Sorted array:", sorted_numbers)
