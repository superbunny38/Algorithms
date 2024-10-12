import math
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        len_x, len_y = len(grid),len(grid[0])
        memoi = []
        for _ in range(len(grid)):
            memoi.append([math.inf]*len(grid[0]))
        memoi[0][0] = grid[0][0]
        for i in range(1,len_x):
            memoi[i][0] = memoi[i-1][0]+grid[i][0]
        for j in range(1,len_y):
            memoi[0][j] = memoi[0][j-1]+grid[0][j]
        for i in range(1,len_x):
            for j in range(1,len_y):
                memoi[i][j] = min(memoi[i-1][j]+grid[i][j],memoi[i][j-1]+grid[i][j])
        return memoi[-1][-1]
