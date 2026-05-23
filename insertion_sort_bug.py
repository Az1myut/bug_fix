def insertion_sort(arr):
    # Traverse from the second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1  # Correct index for insertion sort

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

# Example usage
numbers = [5, 2, 9, 1, 5, 6]

sorted_numbers = insertion_sort(numbers)

print("Sorted array:", sorted_numbers)