#User function Template for python3
from collections import defaultdict
class Solution:
    def countKdivPairs(self, arr, n, k):
        d = defaultdict(list)
        count =0
        for num in arr:
            mod = num%k
            # handle mod == 0 separately
            if mod == 0:
                if 0 in d:
                    count += len(d[0])
            if k-mod in d:
                count+=len(d[k-mod])
            d[mod].append(num)
        return count
