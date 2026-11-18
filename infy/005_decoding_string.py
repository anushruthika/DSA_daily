# # Q5. Number of Decodings of Digit String

# ## Problem Statement

# You are given a string of digits `s`.

# You need to find the number of ways to partition it into valid chunks representing a sequence of decoded symbols.

# A chunk is considered valid if it meets one of the following criteria:

# 1. It is a single digit from `"1"` to `"9"`.
# 2. It is a two-digit string from `"10"` to `"26"` that represents an even number.

# Chunks with leading zeros (e.g., `"0"`, `"04"`) or two-digit strings representing odd numbers (e.g., `"11"`, `"23"`) are strictly invalid.

# Find the number of valid decodings modulo `10^9 + 7`.

# ## Input Format

# The first line contains a string `s`, denoting the digit string.

# ## Constraints

# - 1 ≤ |s| ≤ 10^5

# ## Examples

# ### Example 1

# **Input:**
# ```text
# 126
# ```

# **Output:**
# ```text
# 3
# ```

# **Explanation:**

# The string can be partitioned in 3 valid ways:

# 1. `"1"`, `"2"`, `"6"`
# 2. `"12"`, `"6"` (12 is between 10 and 26 and even)
# 3. `"1"`, `"26"` (26 is between 10 and 26 and even)

# Total valid decodings = 3.

# ### Example 2 (Illustrative)

# **Input:**
# ```text
# 123
# ```

# **Output:**
# ```text
# 2
# ```

# **Explanation:**

# The valid partitions are:

# 1. `"1"`, `"2"`, `"3"`
# 2. `"12"`, `"3"`

# The chunk `"23"` is invalid because it is odd.

# ### Example 3 (Illustrative)

# **Input:**
# ```text
# 102
# ```

# **Output:**
# ```text
# 1
# ```

# **Explanation:**

# The only valid partition is:

# 1. `"10"`, `"2"`

# The single digit `"0"` is invalid, and `"02"` has a leading zero.

# ### Example 4 (Illustrative)

# **Input:**
# ```text
# 226
# ```

# **Output:**
# ```text
# 3
# ```

# **Explanation:**

# The valid partitions are:

# 1. `"2"`, `"2"`, `"6"`
# 2. `"22"`, `"6"`
# 3. `"2"`, `"26"`

# The chunk `"22"` is valid because it is even and between 10 and 26.

