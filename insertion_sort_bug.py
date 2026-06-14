def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1  # Fixed: start comparing with the previous element

        while j >= 0 and arr[j] > key:  # Fixed condition for ascending order
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Fixed: correct position to insert key

    return arr

numbers = [5, 2, 9, 1, 5, 6]

sorted_numbers = insertion_sort(numbers)

print("Sorted array:", sorted_numbers)