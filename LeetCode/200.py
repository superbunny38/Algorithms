from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        length_x = len(grid)
        length_y = len(grid[0])

        def bfs(grid,r,c,length_x, length_y):
            dx = [0,0,1,-1]
            dy = [1,-1,0,0]
            queue = deque([(r,c)])
            
            while queue:
                cur = queue.popleft()
                cur_x,cur_y = cur[0],cur[1]
                # grid[cur_x][cur_y] = 0
                for move_x,move_y in zip(dx,dy):
                    next_x,next_y = cur_x+move_x,cur_y+move_y
                    if 0<=next_x<length_x and 0<=next_y<length_y:
                        if grid[next_x][next_y] == '1':
                            queue.append((next_x,next_y))
                            grid[next_x][next_y] = '0'
        n_islands = 0
        for row_idx in range(length_x):
            for col_idx in range(length_y):
                if grid[row_idx][col_idx] == '1':
                    bfs(grid,row_idx,col_idx,length_x,length_y)
                    n_islands +=1 

        return n_islands
