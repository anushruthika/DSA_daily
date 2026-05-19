# 2570. Merge Two 2D Arrays by Summing Values
# Time Complexity: O(n1 + n2)
# Reason:
# Both arrays are traversed once using two pointers.

# Space Complexity: O(n1 + n2)
# Reason:
# Result array stores merged elements from both arrays.
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m = []
        i=0
        j=0
        n1 = len(nums1)
        n2 = len(nums2)
        while i<n1 and j<n2:
            id1,val1 = nums1[i][0],nums1[i][1]
            id2,val2 = nums2[j][0],nums2[j][1]
            if id1<id2:
                m.append([id1,val1])
                i+=1
            elif id1>id2:
                m.append([id2,val2])
                j+=1
            else:
                m.append([id1,val1+val2])
                i+=1
                j+=1
        while i<n1:
            m.append([nums1[i][0],nums1[i][1]])
            i+=1
        while j<n2:
            m.append([nums2[j][0],nums2[j][1]])
            j+=1
        return m
