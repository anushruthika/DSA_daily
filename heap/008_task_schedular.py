from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        max_val = max(freq.values())
        tasks_with_max_freq = list(freq.values()).count(max_val)
        ans = (
            (max_val - 1) * (n + 1)
            + tasks_with_max_freq
        )
        return max(ans, len(tasks))
# TC: O(n)
# SC: O(1)
# At most 26 uppercase English letters

######## ALSO PRACTICE HEAP 
# TC: O(n log 26) ≈ O(n)
# SC: O(26) ≈ O(1)

from collections import Counter, deque
import heapq

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequency count
        freq = Counter(tasks)
        print(freq)
        # max heap
        # python has min heap so use negative frequencies
        pq = [-count for count in freq.values()]
        heapq.heapify(pq)
        print(pq)
        # stores:
        # (time_when_task_can_be_used_again, remaining_frequency)
        q = deque()
        time = 0
        while pq or q:
            time += 1
            # execute most frequent task
            if pq:
                count = 1 + heapq.heappop(pq)
                # task still remaining
                if count:
                    q.append((time + n, count))
            # cooldown finished
            if q and q[0][0] == time:
                heapq.heappush(pq, q.popleft()[1])
        return time

# # DRY RUN
# A A A B B B B
# | Time | Action    | Heap (Max Freq) | Cooldown Queue    | Schedule                |
# | ---- | --------- | --------------- | ----------------- | ----------------------- |
# | 1    | Execute B | `[-3]`          | `[(3,-3)]`        | B                       |
# | 2    | Execute A | `[]`            | `[(3,-3),(4,-2)]` | B A                     |
# | 3    | Idle      | `[-3]`          | `[(4,-2)]`        | B A idle                |
# | 4    | Execute B | `[-2]`          | `[(6,-2)]`        | B A idle B              |
# | 5    | Execute A | `[]`            | `[(6,-2),(7,-1)]` | B A idle B A            |
# | 6    | Idle      | `[-2]`          | `[(7,-1)]`        | B A idle B A idle       |
# | 7    | Execute B | `[-1]`          | `[(9,-1)]`        | B A idle B A idle B     |
# | 8    | Execute A | `[]`            | `[(9,-1)]`        | B A idle B A idle B A   |
# | 9    | Execute B | `[]`            | `[]`              | B A idle B A idle B A B |

