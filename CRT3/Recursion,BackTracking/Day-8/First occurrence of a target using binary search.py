def findFirstOccurrence(nums, target):
    n = len(nums)
    left, right = 0, n - 1 
    result = -1 
    while left <= right:
        mid = (left + right) // 2 
        if nums[mid] == target:
            result = mid 
            right = mid - 1 
        elif nums[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1 
            
    return result
    
nums = [1, 2, 3, 4, 4, 4, 4, 6, 7]
print(findFirstOccurrence(nums, 4))
print(findFirstOccurrence(nums, 7))
print(findFirstOccurrence(nums, 41))