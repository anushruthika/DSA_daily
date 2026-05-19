# 917. Reverse Only Letters

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        i =0
        arr = list(s)
        n = len(arr)
        j = n-1
        while i<j and i<n and j>=0:
            while i<n and not arr[i].isalpha() :
                i+=1
            while j>=0 and not arr[j].isalpha() :
                j-=1
            if i<n and j>=0 and i<j:
                arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        return "".join(arr)

                

                
