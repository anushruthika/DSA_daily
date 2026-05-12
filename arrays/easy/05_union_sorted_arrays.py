def union_sorted_arrays(arr1, arr2):

    # Time Complexity:
    # O(n + m)
    # set(arr1) → O(n)
    # set(arr2) → O(m)
    # Union | → O(n + m)
    # list(...) → O(n + m)
    # Space Complexity:
    # O(n + m)

    union = []
    return list(set(arr1)|set(arr2))


arr1 = [1, 2, 2, 3, 4, 5]
arr2 = [2, 3, 5, 6, 7]

print(union_sorted_arrays(arr1, arr2))
