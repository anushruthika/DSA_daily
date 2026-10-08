# 1405. Longest Happy String

# chose most freq element: 
# if before two element is == most freq element then pop second most freq element and fill once and append both most freq and second most freq(-1) back to PQ

import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []

        for freq, ch in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if freq:
                heapq.heappush(pq, (-freq, ch))

        ans = []

        while pq:
            freq, ch = heapq.heappop(pq)
            freq = -freq

            # Can't use this character because it would make 3 same
            if len(ans) >= 2 and ans[-1] == ch and ans[-2] == ch:
                if not pq:
                    break

                freq2, ch2 = heapq.heappop(pq)
                freq2 = -freq2

                ans.append(ch2)
                freq2 -= 1

                if freq2:
                    heapq.heappush(pq, (-freq2, ch2))

                heapq.heappush(pq, (-freq, ch))
            else:
                ans.append(ch)
                freq -= 1

                if freq:
                    heapq.heappush(pq, (-freq, ch))

        return ''.join(ans)
