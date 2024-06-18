'''
#parent to child
def findMax(i,n,nums,res):
    if i == n:
        print("Max is :",res)
        return
    if nums[i]>res:
            
            res = nums[i]
    findMax(i+1,n,nums,res)

nums=[12,10,34,54,1]
n=len(nums)
findMax(0,n,nums,nums[0])
'''

#child to parent
def findMax(i,n,nums,res):
    if i == n:       
        return res
    if nums[i]>res:           
        res = nums[i]
    a=findMax(i+1,n,nums,res)        
    return  a    
nums=[12,10,34,54,1]
n=len(nums)
result=findMax(0,n,nums,nums[0])
print(result)


#
def findMaxInWay1(index, nums, n, result):
    if index == n:
        print("Max ele is:", result)
        return 
    if nums[index] > result:
        result = nums[index]
    findMaxInWay1(index + 1, nums, n, result)
 
nums = [12, 32, 11, 10]
result = findMaxInWay1(0, nums, len(nums), 0)
 
 
def findMaxInWay2(index, nums, n):
    if index == n - 1:
        return nums[index]
    nextGreater = findMaxInWay2(index + 1, nums, n)
    if nextGreater < nums[index]:
        return nums[index]
    return nextGreater 
 
nums = [12, 32, 11, 10]
result = findMaxInWay2(0, nums, len(nums))
print("Max ele:", result)