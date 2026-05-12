def missingNum(arr):

    # Time Complexity:
    # O(n)

    # Space Complexity:
    # O(1)

    n = len(arr)

    # Write your main logic here
    return sum(range(1,n+2))-sum(arr)

arr = [8, 2, 4, 5, 3, 7, 1]

print(missingNum(arr))
