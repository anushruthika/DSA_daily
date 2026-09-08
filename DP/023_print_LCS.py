def findLCS(n: int, m: int, text1: str, text2: str) -> str:
    n,m = len(text1),len(text2)
    DP = [[0]*(m+1) for _ in range(n+1)]
    for r in range(n+1):
        DP[r][0] = 0
    for c in range(m+1):
        DP[0][c] = 0
    for r in range(1,n+1):
        for c in range(1,m+1):
            if text1[r-1] == text2[c-1]:
                DP[r][c] = 1+DP[r-1][c-1]
            else:
                DP[r][c] = max(DP[r-1][c],DP[r][c-1])
    r = n
    c = m
    ans = []
    while r>0 and c>0:
            if text1[r-1] == text2[c-1]:
                ans.append(text1[r-1])
                r-=1
                c-=1
            else:
                if DP[r-1][c] > DP[r][c-1]:
                    r-=1
                else:
                    c-=1
    return "".join(ans[::-1])






