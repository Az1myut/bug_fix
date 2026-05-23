def insertion_sort(arr):
    # Traverse from the second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i + 1

        
        # one position ahead
        while j > 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

       
        arr[j + 1] = key

    return arr


# Example usage
numbers = [5, 2, 9, 1, 5, 6]

sorted_numbers = insertion_sort(numbers)

print("Sorted array:", sorted_numbers)