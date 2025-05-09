class Solution:
    def merge(self, l: List[List[int]]) -> List[List[int]]:
        l.sort()
        # print(l)
        a=[l[0]]
        for i in range(1,len(l)):
            if(a[-1][0]<=l[i][0] and a[-1][1]<=l[i][1] and a[-1][1]>=l[i][0]):
                a.append([a[-1][0],l[i][1]])
                a.pop(-2)
                continue
            if(a[-1][0]<=l[i][0] and a[-1][1]>=l[i][1] and a[-1][1]>=l[i][0]):
                continue
            a.append(l[i])
    
# print(a)
            
        return a 
