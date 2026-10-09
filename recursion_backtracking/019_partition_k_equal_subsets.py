# 698. Partition to K Equal Sum Subsets

# same as match stick into square problem but add "tried" set optimization
class Solution:
    def canPartitionKSubsets(self, matchsticks: list[int], k: int) -> bool:
        tot = sum(matchsticks)
        if tot % k != 0:
            return False

        side = tot // k
        matchsticks.sort(reverse=True)
        count = [0] * k
        n = len(matchsticks)
        if matchsticks[0]>side:
            return False
        def dfs(i):
            if i == n:
                return all(x == side for x in count)
            tried = set()
            for ind in range(k):
                if count[ind] in tried:
                    continue
                if matchsticks[i] + count[ind] <= side :
                    tried.add(count[ind])
                    count[ind] += matchsticks[i]
                    if dfs(i + 1):
                        return True

                    count[ind] -= matchsticks[i]

            return False

        return dfs(0)
