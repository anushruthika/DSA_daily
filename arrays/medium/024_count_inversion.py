# arr = [2, 4, 1, 3, 5]

#                  [2, 4, 1, 3, 5]
#                 /               \
#            [2, 4, 1]           [3, 5]
#            /      \             /   \
#          [2]     [4, 1]       [3]   [5]
#                  /   \
#                [4]   [1]


# MERGE:

# [4] + [1]  -> [1, 4]
# Inversions: (4, 1) = 1

# [2] + [1, 4] -> [1, 2, 4]
# Inversions: (2, 1) = 1

# [3] + [5] -> [3, 5]
# Inversions: 0

# [1, 2, 4] + [3, 5] -> [1, 2, 3, 4, 5]
# Inversions: (4, 3) = 1


# Total inversion count = 1 + 1 + 0 + 1 = 3

# Inversion pairs:
# (2, 1), (4, 1), (4, 3)


class Solution:
    def inversionCount(self, arr):
        # code here
        def merge_sort(a):
            n = len(a)
            if n<=1:
                return a,0
            mid = n//2
            left ,lc = merge_sort(a[:mid])
            right, rc = merge_sort(a[mid:])
            count = lc+rc
            ans = []
            i = 0
            j = 0
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:
                    
                    ans.append(left[i])
                    i+=1
                else:
                    count+=len(left)-i
                    ans.append(right[j])
                    j+=1
            ans.extend(left[i:])
            ans.extend(right[j:])
            return ans,count
        _,c = merge_sort(arr)
        return c
