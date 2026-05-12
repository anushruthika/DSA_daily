def linear_search(arr, x):

    # Time Complexity:
    # Best Case  : O(1)
    # Worst Case : O(n)

    # Space Complexity:
    # O(1)

    for i in range(len(arr)):

        # Check if element is found
        if arr[i] == x:
            return i

    # Element not found
    return -1


arr = [1, 2, 3, 4, 5, 6, 7]
x = 6

print(linear_search(arr, x))
