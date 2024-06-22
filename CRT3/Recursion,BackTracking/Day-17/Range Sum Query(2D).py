class NumMatrix:
    def __init__(self, matrix):
        self.cache = []
        m, n = len(matrix), len(matrix[0])
        
        for row in range(m):
            currRow = [0] * n
            self.cache.append(currRow)
            for col in range(n):
                curr = matrix[row][col]
                if row - 1 >= 0:
                    curr += self.cache[row - 1][col]
                if col - 1 >= 0:
                    curr += self.cache[row][col - 1]
                if row - 1 >= 0 and col - 1 >= 0:
                    curr -= self.cache[row - 1][col - 1]
                self.cache[row][col] = curr

    def sumRegion(self, row1, col1, row2, col2):
        big = self.cache[row2][col2]
        upper, left, common = 0, 0, 0 
        if row1 > 0:
            upper = self.cache[row1 - 1][col2]
        if col1 > 0:
            left = self.cache[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            common = self.cache[row1 - 1][col1 - 1]
        return big - upper - left + common

matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
num_matrix = NumMatrix(matrix)

print(num_matrix.sumRegion(2, 1, 4, 3))  # Output: 8
print(num_matrix.sumRegion(1, 1, 2, 2))  # Output: 11
print(num_matrix.sumRegion(1, 2, 2, 4))  # Output: 12
