# 1899. Merge Triplets to Form Target Triplet

class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        n = len(triplets)
        forbiden = set()
        for i in range(n):
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] >target[2]:
                forbiden.add(i)
        boolA= False
        boolB= False
        boolC = False
        for i in range(n):
            if i not in forbiden:
                if not boolA and triplets[i][0] == target[0]:
                    boolA = True
                if not boolB and triplets[i][1] == target[1]:
                    boolB = True
                if not boolC and triplets[i][2] == target[2]:
                    boolC = True

        return boolA and boolB and boolC
