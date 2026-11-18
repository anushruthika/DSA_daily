# # Q10. Heist Season

# ## Problem Statement

# A crew of `n` members plans a season of heists. Each heist `i` (from 1 to N) requires `g[i]` members and yields loot worth `p[i]`.

# Each crew member can work on at most one heist, meaning the total number of members used across all chosen heists must not exceed `n`.

# There are two special mechanics:

# ### 1. The Fence's Cut

# Loot must be fenced, and the fence charges a flat fee `F` per chosen heist.

# If the chosen heists yield a total loot of `P` and there are `K` chosen heists, the crew's take-home profit is:

# `P - K * F`

# The crew's take-home profit must be at least `minTake`.

# ### 2. The Inside Man

# The crew has exactly one insider who can be assigned to at most one chosen heist.

# If the insider is assigned to heist `i`, that heist requires:

# `ceil(g[i] / 2)` members instead of `g[i]`.

# The insider is not a crew member, so assigning him does not consume any of the `n` crew members.

# Using the insider is optional.

# A plan consists of selecting a subset of heists, and optionally choosing at most one heist from that subset to assign the insider to.

# ## Example 1

# **Input:**
# ```text
# 5 3
# 3 4 2
# 10 12 7
# 2 15
# ```

# Parameters:
# - n = 5 (crew members)
# - N = 3 (number of heists)
# - g = [3, 4, 2]
# - p = [10, 12, 7]
# - F = 2
# - minTake = 15

# **Explanation:**

# Consider selecting heists 1 and 2.

# Without the insider:
# - Heist 1 requires 3 members.
# - Heist 2 requires 4 members.
# - Total = 7 members.
# - This exceeds the available 5 members.

# Now assign the insider to heist 2.

# Modified requirement:

# `ceil(4 / 2) = 2`

# Total crew members required:

# `3 + 2 = 5`

# Total loot:

# `10 + 12 = 22`

# Number of selected heists = 2.

# Fence charges:

# `2 * 2 = 4`

# Take-home profit:

# `22 - 4 = 18`

# Since 18 >= 15, this is a valid plan.

# **Example 2: Selecting heists 1 and 3**

# Crew members required:

# `3 + 2 = 5`

# Total loot:

# `10 + 7 = 17`

# Fence charges:

# `2 * 2 = 4`

# Take-home profit:

# `17 - 4 = 13`

# Since 13 < 15, this plan is invalid.

# ## Example 3: Using the insider on different heists

# Using the same input, select heists 2 and 3.

# **Case 1: Insider assigned to heist 2**

# - Heist 2 requires ceil(4/2) = 2 members.
# - Heist 3 requires 2 members.
# - Total crew members = 4.
# - Total profit = 12 + 7 - 4 = 15.

# Valid because 15 >= minTake.

# **Case 2: Insider assigned to heist 3**

# - Heist 2 requires 4 members.
# - Heist 3 requires ceil(2/2) = 1 member.
# - Total crew members = 5.
# - Total profit = 12 + 7 - 4 = 15.

# This is also valid.

# These are two distinct plans because the insider is assigned to different heists.

# ## Important Conditions

# 1. Total crew members used must not exceed n.
# 2. Each crew member can work on at most one heist.
# 3. The insider can be assigned to at most one selected heist.
# 4. The insider reduces the assigned heist's crew requirement to ceil(g[i]/2).
# 5. Using the insider is optional.
# 6. Take-home profit must be at least minTake.


# n member, N heists[g1,g2..gN] [p1,p2,pN]requires g[i] members. 
# F per chosen heist cost. i.e Total P-f*K.
# in one of the heists i cna use insider. for that i need g[i]/2 ceil members
# n = 5
# N = 3
#      1  2  3
# g = [3, 4, 2]
# p = [10, 12, 7]
# F = 2
# minTake = 15
# 1,2 => 2 18 | 2,3 => 2 15| 2,3=> 3 15
# ans: 18
# # 10+12-2*2 = 18
import math
from functools import lru_cache
def solve(n, N, g, p, F, minTake):
    @lru_cache(None)
    def dfs(mem,ind,tot,cnt,take):
        if ind == N:
            if (tot-cnt*F)>=minTake:
                return 1
            return 0
        count = 0
        # take
        if mem>=g[ind]:
            count = dfs(mem-g[ind],ind+1,tot+p[ind],cnt+1,take)
        # not take
        count+=dfs(mem,ind+1,tot,cnt,take)
        # take & insider
        if take == 0 and mem>=math.ceil(g[ind]/2):
            count += dfs(mem-math.ceil(g[ind]/2),ind+1,tot+p[ind],cnt+1,1)
        return count
    return dfs(n,0,0,0,0)
tests = [
    (5, 3, [3, 4, 2], [10, 12, 7], 2, 15, 3),
    (5, 3, [3, 4, 2], [10, 12, 7], 2, 18, 1),
    (3, 2, [2, 3], [10, 15], 2, 10, 2),
    (4, 3, [2, 3, 4], [8, 12, 15], 3, 15, 1),
    (10, 4, [2, 3, 4, 5], [10, 20, 30, 40], 5, 30, 30)
]

for i, (n, N, g, p, F, minTake, expected) in enumerate(tests, 1):

    result = solve(n, N, g, p, F, minTake)

    print(f"Test {i}: {'PASS' if result == expected else 'FAIL'}")
    print("Expected:", expected)
    print("Your output:", result)
    print()
