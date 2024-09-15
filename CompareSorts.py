import time
import random
import pandas as pd

from HeapSortImplementation import heapsort
 
# Quicksort implementation
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

def run_comparison():
    sizes = [1000, 5000, 10000, 50000, 100000]
    sorts = ['Sorted', 'Reverse-Sorted', 'Random']

    # Initialize an empty list to hold the result rows
    results = []

    for size in sizes:
        for sort_type in sorts:
            if sort_type == 'Sorted':
                arr = list(range(size))
            elif sort_type == 'Reverse-Sorted':
                arr = list(range(size, 0, -1))
            else:
                arr = random.sample(range(size), size)

            arr1, arr2, arr3 = arr[:], arr[:], arr[:]

            heapsort_time = measure_time(heapsort, arr1)
            quicksort_time = measure_time(quicksort, arr2)
            merge_sort_time = measure_time(merge_sort, arr3)

            # Append the results as a new row
            results.append([size, sort_type, heapsort_time, quicksort_time, merge_sort_time])

    # Create a DataFrame from the results
    df = pd.DataFrame(results, columns=["Array Size", "Array Type", "Heapsort Time (s)", "Quicksort Time (s)", "Merge Sort Time (s)"])
    print(df)

# Run the comparison
print("\n Running Emperical Comparisons")
run_comparison()
