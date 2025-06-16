class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid) #|
        m = len(grid[0]) #<->
        islands=0

        def dfs(i,j):
            if i<0 or i>=n or j>=m or j<0 or grid[i][j] is not '1': #up, down, right, left
                return
            else: 
                grid[i][j] = '0'
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i-1,j)


        for i in range(n):
            for j in range(m):
                if grid[i][j] is '1':
                    islands += 1
                    dfs(i,j)
        
        return islands
        
        
