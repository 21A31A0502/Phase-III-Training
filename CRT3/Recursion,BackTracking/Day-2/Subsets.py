# Write a python program to print all possible subsets of a given list. 
#	nums = [10, 11, 12, 13, 14]
'''
 ==> Write a python program to print all possible subsets of a given list. 
	nums = [10, 11, 12, 13, 14]
	[]
	[10]
	[11]
	[12]
	[13]
	[14]
	[10, 11]
	[10, 12]
	[10, 13]
	[10, 14]
	[11, 12]
	[11, 13]
	[11, 14]
	[10, 11, 12]
	[10, 11, 13]
	[10, 11, 14]
	[10, 11, 12, 13]
	[10, 11, 12, 14]
 '''
 
def printAllSubsets(nums, index, result, value):
    
    if index == len(nums):
        
        print(result)
        value[0] += 1
        return
 
    # Include 
    result.append(nums[index])
    printAllSubsets(nums, index + 1, result, value)
    result.pop()
 
    # Exclude
    printAllSubsets(nums, index + 1, result, value)
 
nums = [10, 20, 30, 40, 50, 60, 65]
 
value = [0]
printAllSubsets(nums, 0, [], value)
print(value[0])