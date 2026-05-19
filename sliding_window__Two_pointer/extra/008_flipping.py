# 832. Flipping an Image

# Time Complexity: O(m * n)
# SC = O(m)
class Solution:
    def flip(self,arr,n):
        i = 0
        j = n-1
        while i<j:
            arr[i],arr[j] = 1-arr[j],1-arr[i]
            i+=1
            j-=1
        if n%2==0:
            return arr
        else:
            arr[n//2]=1-arr[n//2]
            return arr
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image[0])
        res = []
        for arr in image:
            res.append(self.flip(arr,n))
        return res
            
