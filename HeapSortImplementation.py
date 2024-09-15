def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1  # left child
    right = 2 * i + 2  # right child

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def heapsort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

# Example usage
arr = [12, 11, 13, 5, 6, 7, 15]
heapsort(arr)
print("Sorted array is:", arr)
