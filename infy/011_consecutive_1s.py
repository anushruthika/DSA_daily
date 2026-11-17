# # Q11. Quantum Plasma Resonance

# ## Problem Statement

# You are configuring a linear sequence of exactly N plasma nodes. Each node must be calibrated to a specific intensity level from 1 to F (inclusive).

# Under normal circumstances, the total power output of the sequence is simply the sum of all individual node intensities. However, the sequence requires exactly one Fusion Coil to remain stable. You must install the Fusion Coil exactly between two adjacent plasma nodes.

# The coil physically merges the two adjacent nodes, causing their intensities to multiply rather than add. The remaining N − 2 nodes in the sequence continue to add their intensities to the total.

# For example, if N = 4 and the coil is placed between node 2 and node 3, the total power equation becomes:

# I[1] + (I[2] × I[3]) + I[4].

# The final total power output of the sequence must equal exactly T.

# Find the total number of valid configurations.

# A configuration is distinct if:
# - The sequence of N intensities is different.
# - The geometric position of the Fusion Coil is different.

# Since the answer can be very large, return it modulo 10^9 + 7.

# ## Examples

# ### Example 1

# **Input:**
# ```text
# 2 3 2
# ```

# **Explanation:**

# N = 2, F = 3, T = 2.

# Possible intensities are 1, 2, 3.

# Since there are only two nodes, the Fusion Coil must be placed between them.

# Equation:

# I[1] × I[2] = 2

# Valid configurations:
# - [1, 2] → 1 × 2 = 2
# - [2, 1] → 2 × 1 = 2

# Total valid configurations = 2.

# **Output:**
# ```text
# 2
# ```

# ### Example 2

# **Input:**
# ```text
# 3 2 3
# ```

# **Explanation:**

# N = 3, F = 2, T = 3.

# Possible intensities are 1 and 2.

# There are two possible Fusion Coil positions.

# **Case 1: Coil between node 1 and node 2**

# Equation:

# I[1] × I[2] + I[3] = 3

# Valid configurations:
# - [1, 1, 2] → 1 × 1 + 2 = 3
# - [1, 2, 1] → 1 × 2 + 1 = 3
# - [2, 1, 1] → 2 × 1 + 1 = 3

# Count = 3.

# **Case 2: Coil between node 2 and node 3**

# Equation:

# I[1] + I[2] × I[3] = 3

# Valid configurations:
# - [2, 1, 1] → 2 + 1 × 1 = 3
# - [1, 1, 2] → 1 + 1 × 2 = 3
# - [1, 2, 1] → 1 + 2 × 1 = 3

# Count = 3.

# Total valid configurations = 3 + 3 = 6.

# **Output:**
# ```text
# 6
# ```

# ### Example 3

# **Input:**
# ```text
# 3 3 5
# ```

# **Explanation:**

# N = 3, F = 3, T = 5.

# Possible intensities are 1, 2 and 3.

# There are two possible Fusion Coil positions.

# **Case 1: Coil between node 1 and node 2**

# Equation:

# I[1] × I[2] + I[3] = 5

# Valid configurations:
# - [1, 2, 3] → 1 × 2 + 3 = 5
# - [2, 1, 3] → 2 × 1 + 3 = 5
# - [2, 2, 1] → 2 × 2 + 1 = 5

# Count = 3.

# **Case 2: Coil between node 2 and node 3**

# Equation:

# I[1] + I[2] × I[3] = 5

# Valid configurations:
# - [3, 1, 2] → 3 + 1 × 2 = 5
# - [3, 2, 1] → 3 + 2 × 1 = 5
# - [1, 2, 2] → 1 + 2 × 2 = 5

# Count = 3.

# Total valid configurations = 3 + 3 = 6.

# **Output:**
# ```text
# 6
# ```

# ## Summary of Examples

# | Example | N | F | T | Output |
# |---|---:|---:|---:|---:|
# | 1 | 2 | 3 | 2 | 2 |
# | 2 | 3 | 2 | 3 | 6 |
# | 3 | 3 | 3 | 5 | 6 |

# ## Output Format

# Return the total number of valid configurations modulo 10^9 + 7.



def solve(N, F, T):
    from functools import lru_cache
    @lru_cache(None)
    def rec(ind,mul,cur,prev):
        if ind == N:
            if cur == T and mul==1:
                return 1
            return 0
        s = 0
        for i in range(1,F+1):
            s+=rec(ind+1,mul,cur+i,i)
            if mul==0 and prev!=None:
                s+=rec(ind+1,1,cur-prev+prev*i,i)
        return s
    return rec(0,0,0,None)

# 12, 21
# 112, 121,211
# 123, 

tests = [
    (2, 3, 2),
    (3, 2, 3),
    (3, 3, 5),
    (3, 2, 5),
    (4, 2, 5)
]

for test in tests:
    print(test, "->", solve(*test))
