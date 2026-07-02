# 1482. Minimum Number of Days to Make m Bouquets
# Brute Force: O(n * (maxDay - minDay + 1))
# Optimal (Binary Search): O(n * log(maxDay - minDay))
# Space: O(1)
class Solution:
    def possible_bouquets(self,bloomDay,day,k):
        counter = 0
        bouquet = 0
        for i in bloomDay:
            if i<=day:
                counter+=1
            else:
                if counter!=0:
                    bouquet += counter//k
                counter = 0
        if counter!=0:
            bouquet += counter//k
        return bouquet
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low = min(bloomDay)
        high = max(bloomDay)
        ans = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            bq = self.possible_bouquets(bloomDay, mid, k)

            if bq >= m:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
