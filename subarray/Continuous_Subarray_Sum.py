# Continous Subarray Sum  Leet code: 523
/** This code checks if a continuous subarray of at least two elements has a sum that is a multiple of k. 
It uses the remainder of the prefix sum modulo k to track patterns.
If the same remainder appears again at a distance of more than one index, the subarray sum between them is divisible by k. 
A dictionary stores the earliest index for each remainder. **/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {}           # Dictionary to store {remainder: index}
        s = 0            # Cumulative sum
        
        for i in range(0, len(nums)):
            s += nums[i]                 # Update the running sum
            if s % k == 0 and i != 0:    # If sum is divisible by k and subarray length ≥ 2
                return True
            rem = s % k                  # Compute remainder of current sum with k
            if (rem in d) and (i - d[rem] > 0):  # If remainder seen before and gap ≥ 1
                return True
            elif rem not in d:           # Store first occurrence of this remainder
                d[rem] = i + 1
        
        return False                     # No valid subarray found
