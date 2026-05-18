# 904. Fruit Into Baskets

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i=0
        j=0
        # max_fruits
        mf = 0
        d = defaultdict(int)
        s = set()
        while j<len(fruits):
            d[fruits[j]]+=1
            s.add(fruits[j])
            while len(s)>2:
                d[fruits[i]]-=1
                if d[fruits[i]] == 0:
                    s.remove(fruits[i])
                i+=1
            mf = max(mf, j - i + 1)
            j+=1
        return mf
