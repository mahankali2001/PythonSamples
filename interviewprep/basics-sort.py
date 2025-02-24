def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage
numbers = [64, 25, 12, 22, 11, 90]
bubble_sort(numbers)
print("Bubble sorted array is:", numbers)

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
numbers = [64, 25, 12, 22, 11, 90]
selection_sort(numbers)
print("Selection sorted array is:", numbers)

