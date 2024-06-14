

def isPresentInMatrix(matrix, target):
    n, m = len(matrix), len(matrix[0])
    left, right = 0, (n * m) - 1 
    
    while left <= right:
        mid = (left + right) // 2 
        row = mid // m 
        col = mid % m 
        if matrix[row][col] == target:
            return True 
        elif matrix[row][col] > target:
            right = mid - 1 
        else:
            left = mid + 1 
    return False
        
matrix = [[10, 20, 30, 40], 
            [50, 60, 70, 80], 
            [90, 100, 110, 120]]
            
target = 100 
if isPresentInMatrix(matrix, target):
    print(target, "found")
else:
    print(target, "not found")
    
    
    
