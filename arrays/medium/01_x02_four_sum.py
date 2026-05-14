# Time Complexity: O(n³)
# Space Complexity: O(n)

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums.sort()
        for i in range(n-3):
            for j in range(i+1,n-2):
                l = j+1
                r = n-1
                while l<r:
                    total = nums[i]+nums[j]+nums[l]+nums[r]
                    if total<target:
                        l+=1
                    elif total>target:
                        r-=1
                    else:
                        res.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                        r-=1
        return list(res)

# Time Complexity: O(n³)
# Space Complexity: O(1)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 3):
            # skip duplicate starting values
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums) - 2):
                # skip duplicate starting values
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, len(nums) - 1

                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif four_sum < target:
                        left += 1
                    else:
                        right -= 1
        return res
