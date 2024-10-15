def quicksort(arr):
    if len(arr) <= 1:  # Base case: array is already sorted if it has 0 or 1 element
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose the pivot (e.g., middle element)
    left = [x for x in arr if x < pivot]  # Elements smaller than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements larger than the pivot
    
    return quicksort(left) + middle + quicksort(right)  # Recursively sort and combine
