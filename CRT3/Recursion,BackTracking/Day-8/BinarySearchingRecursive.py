def findUsingBinarySearch(nums, target, left, right):
    if left > right:
        return -1 
 
    mid = (left + right) // 2 
    if nums[mid] == target:
        return mid 
    elif nums[mid] > target:
        return findUsingBinarySearch(nums, target, left, mid - 1)
    return findUsingBinarySearch(nums, target, mid + 1, right)
 
nums = [8, 7, 6, 6, 5, 90, 1, 2, 21]
nums = sorted(nums)
print(nums)
target = 900
index = findUsingBinarySearch(nums, target, 0, len(nums) - 1)
if index == -1:
    print(target, "not found")
else:
    print(target, "found at index:", index)