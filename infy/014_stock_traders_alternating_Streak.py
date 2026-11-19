N = 5
M = 2
p = [1, 5, 2, 6, 3]

def solve(N, M, p):
    muligan = 1
    def rec(ind,muligan_left,prev,updown):
        if ind == N:
            return 0
        cur = 0
        if prev==None:
            # take
            return max(1+rec(ind+1,muligan_left,p[ind],None),rec(ind+1,muligan_left,None,None))
        elif abs(p[ind]-prev)>=M:
            if updown and ( updown==1 and p[ind]-prev<0) or (updown==0 and p[ind]-prev>0):
                cur = max(cur,1+rec(ind+1,muligan_left,p[ind],1-updown))
            elif not updown:
                if p[ind]>prev:
                    cur = max(cur,1+rec(ind+1,muligan_left,p[ind],1))
                elif p[ind]<prev:
                    cur = max(cur,1+rec(ind+1,muligan_left,p[ind],0))
                elif muligan_left!=0:
                    cur = max(cur,1+rec(ind+1,muligan_left-1,p[ind],None))
            # use muligan
            elif muligan_left!=0:
                if p[ind]>prev:
                    cur = max(cur,1+rec(ind+1,muligan_left-1,p[ind],1))
                elif p[ind]<prev:
                    cur = max(cur,1+rec(ind+1,muligan_left-1,p[ind],0))
                else:
                    # flat
                    cur = max(cur,1+rec(ind+1,muligan_left-1,p[ind],None))
        # not_take
        cur = max(cur,rec(ind+1,muligan_left,prev,updown))
        return cur
    return rec(0,1,None,None)


test_cases = [
    # (N, M, prices, expected_output)

    # Test 1: Already alternating
    (5, 2, [1, 5, 2, 6, 3], 5),

    # Test 2: Completely increasing (one mulligan)
    (5, 2, [1, 3, 5, 7, 9], 3),

    # Test 3: Completely decreasing (one mulligan)
    (5, 2, [10, 8, 6, 4, 2], 3),

    # Test 4: Noise threshold restriction
    (5, 3, [1, 2, 5, 3, 8], 3),

    # Test 5: Alternating sequence
    (6, 1, [2, 7, 3, 9, 4, 10], 6),

    # Test 6: All elements equal
    (5, 1, [4, 4, 4, 4, 4], 1),

    # Test 7: Alternating sequence with M = 2
    (6, 2, [1, 4, 2, 5, 3, 6], 6),

    # Test 8: Increasing sequence with larger threshold
    (6, 3, [1, 2, 3, 4, 5, 6], 2),

    # Test 9: Alternating sequence starting downward
    (7, 2, [8, 1, 7, 2, 6, 3, 5], 7),

    # Test 10: Mulligan not needed
    (4, 5, [1, 10, 2, 11], 4),

    # Test 11: Single element
    (1, 1, [9], 1),

    # Test 12: Increasing sequence
    (4, 1, [1, 2, 3, 4], 3),
]


for i, (N, M, p, expected) in enumerate(test_cases, 1):
    result = solve(N, M, p)

    status = "PASS" if result == expected else "FAIL"

    print(
        f"Test {i}: {status} | "
        f"Expected: {expected}, Got: {result}"
    )
