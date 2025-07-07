class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
            else:
                if i-d[nums[i]] <=k:
                    return True
                else:
                    d[nums[i]]=i
        return False
