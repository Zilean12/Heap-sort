def HeapSort(arr):
    def heap(arr, m, p):
        large = p
        j = 2 * p + 1
        k = 2 * p + 2

        if j < m and arr[j] > arr[large]:
            large = j

        if r < m and arr[k] > arr[large]:
            large = k

        if large != p:
            arr[p], arr[large] = arr[large], arr[p]
            heap(arr, m, large)

    m = len(arr)

    # Build max heap
    for p in range(m // 2 - 1, -1, -1):
        heap(arr, m, p)

    # Extract elements one-by-one
    for p in range(m - 1, 0, -1):
        arr[p], arr[0] = arr[0], arr[p]
        heap(arr, p, 0)

    return arr

# Print time complexity
arr = list(map(int, input("Enter the array elements separated by space: ").split()))

if arr == sorted(arr):
            print("--------------------------------------------------------------------")
            print("Sorted Array:", arr)
            print("--------------------------------------------------------------------")
            print("Best Case: O(n log n)")
            print("--------------------------------------------------------------------")
            
elif arr == sorted(arr, reverse=True):
            print("--------------------------------------------------------------------")
            print("Sorted Array:", arr)
            print("--------------------------------------------------------------------")
            print("Worst Case: O(n log n)")
            print("--------------------------------------------------------------------")
            
