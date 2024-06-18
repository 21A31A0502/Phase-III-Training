'''
#Parent to child 
def findMin(i,n,nums,res):
    if i == n:
        print("Min is :",res)
        return
    if nums[i]<res:
            
            res = nums[i]
    findMin(i+1,n,nums,res)

nums=[12,10,34,54,1]
n=len(nums)
findMin(0,n,nums,nums[n-1])

'''

#child to parent 
def findMin(i,n,nums,res):
    if i == n:
        
        return res
    if nums[i]<res:
            
        res = nums[i]
    a=findMin(i+1,n,nums,res)        
    return  a    

nums=[12,10,34,54,100]
n=len(nums)
result=findMin(0,n,nums,nums[n-1])
print(result)
