# TC : o(nlogn) SC:O(1)
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        i=0
        j=n-1
        count=0

        while i<j:
            if nums[i]+nums[j]<target:
                count+=j-i
                i+=1
            else:
                j-=1  
        return count


# DRY run 1       
# [-1,1,2,3,1] 
# [-1,1,1,2,3] 
# i=0 , j=3 , 3+-1 !< 2 , count = 0
# i =0, j=2 , 2+-1 < 2  , count = j-i+1 => 3 => adding all possiblities [-1,2],[-1,1],[-1,1]
# i =1, j=2 , 2+1  !<2. , count = 3 


# DRY RUN 2
# [9,-5,-5,5,-5,-4,-6,6,-6] target =3
# sorted => [-6,-6,-5,-5,-5,-4,5,6,9] n = 8

# i=0 ,j=n-1, n[i]+n[j] <3 , count = 0
# i=0 , j=8 , -6+9 !< 3 , count = 0 => j-=1
# i=0 , j=7 , -6+6 < 3 , count = 7-0 = 7 => possibliies [-6,6],[-6,5],[-6,-4],[-6,-5],[-6,-5],[-6,-5],[-6,-6] =>i+=1
# i=1 , j=7 , -6+6 < 3 , count = 7-1 = 6 => possiblities [-6,-5],[-6,-5],[-6,-5],[-6,-4],[-6,5],[-6,6]  => i+=1
# i=2 , j=7 , -5+6 < 3 , count = 7-2 = 5 i+=1
# i=3 , j=7 , -5+6 < 3 , count = 7-3 = 4 i+=1
# i=4 , j=7 , -5+6 < 3 , count = 7-4 = 3 i+=1
# i=5 , j=7 , -4+6 < 3 , count = 7-5 = 2 i+=1
# i=6 , j=7 , 5+6 < 3 , count = 7-6 = 1 i+=1
# sum(count) = 7+6+5+4+3+2+1 = 
