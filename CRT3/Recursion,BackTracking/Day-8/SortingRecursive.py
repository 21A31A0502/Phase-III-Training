def performBubbleSort(nums, n):
    if n == 1:
        return    
    # last index is (n - 1)
    for index in range(n - 1):
        if nums[index] > nums[index + 1]:
            nums[index], nums[index + 1] = nums[index + 1], nums[index]
    performBubbleSort(nums, n - 1)    
def performSelectionSort(nums, n):
    if n == 1:
        return 
    # fix (n-1)th index 
    maxEleIndex = n - 1 
    for index in range(n - 1):
        if nums[index] > nums[maxEleIndex]:
            maxEleIndex = index 
    if maxEleIndex != n - 1:
        nums[maxEleIndex], nums[n - 1] = nums[n - 1], nums[maxEleIndex]
    performSelectionSort(nums, n - 1)
def performInsertionSort(nums, n):
    if n == 1:
        return    
    performInsertionSort(nums, n - 1)
    # nums = [1, 3, 4, 5, 6, 7, 8, 2]
    # nums = [1, 3, 3, 4, 5, 6, 7, 8]
    currValue = nums[n - 1]
    prevIndex = n - 2
    while prevIndex >= 0:
        if nums[prevIndex] > currValue:
            nums[prevIndex + 1] = nums[prevIndex]
        else:
            break 
        prevIndex -= 1 
    nums[prevIndex + 1] = currValue


def mergeThoseTwoArrays(nums, left, mid, right):
    # left subarray --> [left, mid]
    # right subarray --> [mid + 1, right]
    temp = []
    index1 = left 
    index2 = mid + 1 
    
    while index1 <= mid and index2 <= right:
        if nums[index1] > nums[index2]:
            temp.append(nums[index2])
            index2 += 1 
        else:
            temp.append(nums[index1])
            index1 += 1 
    
    while index1 <= mid:
        temp.append(nums[index1])
        index1 += 1 
        
    while index2 <= right:
        temp.append(nums[index2])
        index2 += 1 
        
    
    position = 0 
    for index in range(left, right + 1):
        nums[index] = temp[position]
        position += 1 
        
        
        
   


def divideAndMerge(nums, left, right):
    if left >= right:
        return 
    
    mid = (left + right) // 2 
    # left subarray --> [left, mid]
    # right subarray --> [mid + 1, right]
    
    divideAndMerge(nums, left, mid)
    divideAndMerge(nums, mid + 1, right)
    mergeThoseTwoArrays(nums, left, mid, right)
    
    
    


def performMergeSort(nums):
    n = len(nums)
    divideAndMerge(nums, 0, n - 1)


def getPivotIndex(nums, left, right):
    pivot = nums[right]
    # [18, 12, 22, 23, 10, 7, 20]
     # [18, 12, 10, 23, 22, 7, 20]
     # [18, 12, 10, 7, 22, 23, 20]
     
     
     
    # [18, 12, 10, 7, 22, 23, 20]
    # [18, 12, 10, 7, 20, 23, 22]
    position = left
    for index in range(left, right):
        if nums[index] < pivot:
            nums[index], nums[position] = nums[position], nums[index]
            position += 1 
    
    nums[right], nums[position] = nums[position], nums[right]
    return position

    

def findPivotAndSort(nums, left, right):
    if left >= right:
        return 
    pivotIndex = getPivotIndex(nums, left, right)
    findPivotAndSort(nums, left, pivotIndex - 1)
    findPivotAndSort(nums, pivotIndex + 1, right)
    
def performQuickSort(nums):
    n = len(nums)
    findPivotAndSort(nums, 0, n - 1)  





nums = [8, 1, 7, 6, 5, 4, 3, 2]
print("Before sorting:", nums)
performSelectionSort(nums, len(nums))
print("After sorting:", nums)
performBubbleSort(nums, len(nums))
print("After sorting:", nums)
performInsertionSort(nums, len(nums))
print("After sorting:", nums)
performMergeSort(nums)
print("After sorting:", nums)
performQuickSort(nums)
print("After sorting:", nums)
