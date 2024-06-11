def linear_recursive(nums,target,index,n):
    if index==n:
        return -1 
    elif nums[index]==target:
        return index 
    return linear_recursive(nums,target,index+1,n)


nums=[8,4,6,2,9,12]
target=50
index=linear_recursive(nums,target,0,len(nums))
if index==-1:
    print(target,"Not Found")
else:
    print(target,"Found at index:",index)    
