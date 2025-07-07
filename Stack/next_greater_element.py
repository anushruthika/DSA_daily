nums=[4,8,5,2,25]
nums=[6,8,0,1,3]
stack=[]
n=len(nums)
res=[-1]*n
for i in range(n):
    while stack and nums[stack[0]]<nums[i]:
        res[stack.pop(0)]=nums[i]
    stack.insert(0,i)
print(res)
        
