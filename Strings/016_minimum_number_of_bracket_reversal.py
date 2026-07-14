# https://www.geeksforgeeks.org/problems/count-the-reversals0401/1

# Brute Force: Generate all 2^n possible strings by either reversing or not reversing each bracket, 
check which resulting strings are balanced, and return the minimum number of reversals among them.
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n)

  
# STACK APPROACH
# Time Complexity: O(n)
# Space Complexity: O(1)
def countminreversals(s):
    if len(s) % 2:
        return -1
    stack = []
    # m- number of {
    count_m = 0
    # n- number of }
    count_n = 0
    for i in s:
        if i == '{':
            count_m+=1
            stack.append('{')
        else:
            if stack and stack[-1] == '{':
                count_m -=1
                stack.pop()
            else:
                count_n+=1
                stack.append(')')
    return math.ceil(count_m/2)+math.ceil(count_n/2)


# optimization
# Time Complexity: O(n)
# Space Complexity: O(1)
# You don't actually need the stack. You only need the number of unmatched opening and closing braces.
