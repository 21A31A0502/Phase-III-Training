class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for i in range(m)]
        atlantic = [[False] * n for i in range(m)]   
        def visitAllNodes(row, col, ocean):
            if ocean[row][col]:
                return 
            ocean[row][col] = True 
            Q = [[row, col]]
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while Q:
                curr = Q.pop(0)
                for direction in directions:
                    newRow = curr[0] + direction[0]
                    newCol = curr[1] + direction[1]
                    
                    if newRow >= 0 and newCol >= 0 and newRow < m and newCol < n and ocean[newRow][newCol] == False and heights[newRow][newCol] >= heights[curr[0]][curr[1]]:
                        ocean[newRow][newCol] = True 
                        Q.append([newRow, newCol])
                
        
        for row in range(m):
            visitAllNodes(row, 0, pacific)
            visitAllNodes(row, n - 1, atlantic)
            
        for col in range(n):
            visitAllNodes(0, col, pacific)
            visitAllNodes(m - 1, col, atlantic)
            
        result = []
        
        for row in range(m):
            for col in range(n):
                if pacific[row][col] and atlantic[row][col]:
                    result.append([row, col])
        
        return result

# User input
heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]

# Create a Solution object
solution = Solution()

# Call the pacificAtlantic method and print the result
result = solution.pacificAtlantic(heights)
print(result)
