nums = [10, 2, 32, 15, 21, 5, -2]
n = len(nums)
prefix = [0] * n 
for index in range(n):
    prefix[index] = nums[index]
    if index > 0:
        prefix[index] += prefix[index - 1]       
queries = [[0, 6], [1, 6], [4, 5], [2, 6]]
for query in queries:
    left, right = query[0], query[1]
    result = prefix[right]
    if left > 0:
        result -= prefix[left - 1]
    print(result)
    