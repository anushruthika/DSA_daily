# TC:  O(N+klogN)
# SC: O(N)
# global row-wise sorting: eg: [[1,2],[1,3]] k=2 output: 1
import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        arr = []
        for row in matrix:
            arr.extend(row)
        print(arr)
        heapq.heapify(arr)
        while k>1:
            heapq.heappop(arr)
            k-=1

        return heapq.heappop(arr)

##### PLEASE VIEW SOLUTION FOR NO GLOBAL ROW WISE SORTING
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         m = len(matrix)
#         n = len(matrix[0])
#         # 0-indexing
#         # index=r×n+c
#         # r=index//n
#         # c=index%n

#         # 1-indexing
#         # index = rxn+c +1
#         # r= (index−1)//n
#         # c=(index−1)%n
#         return matrix[(k-1)//n][(k-1)%n]


# class Solution:
#     def kthSmallest(self, matrix, k):
#         arr = []
#         for row in matrix:
#             arr.extend(row)
#         return arr[k-1]
