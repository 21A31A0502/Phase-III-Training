'''
def findAllIndices(nums, k, target):
    n = len(nums)
    currTotal = sum(nums[:k])
    result = []
    if currTotal == target:
        result.append(0)
        
    left, right = 0, k 
    while right < n:
        currTotal -= nums[left]
        currTotal += nums[right]
        if currTotal == target:
            result.append(left + 1)
        left += 1 
        right += 1 
    return result

nums = [10, 2, 3, 43, 2, 10, 35, 3]
k = 3 
target = 48
result = findAllIndices(nums, k, target)
print(result)
'''
def maximumSumSubarray (K,Arr,N):
        N = len(Arr)
        currTotal = sum(Arr[:K])
        result =currTotal
       
        left, right = 0, K 
        while right < N:
            currTotal -= Arr[left]
            currTotal += Arr[right]
            result=max(result,currTotal)
            left += 1 
            right += 1 
        return result    
K = 2
Arr = [100, 200, 300, 400]
N = len(Arr)

# Call the function with the inputs
output = maximumSumSubarray(K, Arr, N)
print("Output:", output)            