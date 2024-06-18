class Solution:
    def findAllOnesUsingDFS(self, row, col, grid, n, m):
        if min(row, col) < 0 or row >= n or col >= m or grid[row][col] == 0:
            return 0 
 
        result = 1 
        grid[row][col] = 0
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
 
        for index in range(4):
            newRow = row + dx[index]
            newCol = col + dy[index]
            result += self.findAllOnesUsingDFS(newRow, newCol, grid, n, m)
        return result

    def maxAreaOfIsland(self, grid):
        n = len(grid)
        m = len(grid[0])
        result = 0 
 
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    current = self.findAllOnesUsingDFS(row, col, grid, n, m)
                    result = max(result, current)
        return result 
        
# User input
grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 1, 1]
]

# Create a Solution object
solution = Solution()

# Call the maxAreaOfIsland method and print the result
result = solution.maxAreaOfIsland(grid)
print(result)
