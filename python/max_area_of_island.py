"""
MAX AREA OF ISLAND

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.

source: https://leetcode.com/problems/max-area-of-island/
"""

class Solution:
    def max_area_of_island(self, grid: List[List[int]]) -> int:
        
        grid_width = range(len(grid))
        grid_height = range(len(grid[0]))
        max_area = 0
        
        # Iterate over every coordinate. If we find a one, start a dfs and
        # evaluate if we found a larger island than previous
        for x in grid_width:
            
            for y in grid_height:
                
                if grid[x][y] == 1:
                    max_area = max(max_area, dfs((x,y), grid))
                    
        return max_area

def dfs(coordinate, grid):
    
    x, y = coordinate 
    
    # if we have found a zero('water'), we have to backtrack
    if grid[x][y] == 0:
        return 0 
    
    # we found a 1('land'), and we can set it's are to be 1 
    area = 1
    
    # set the coordinate in the grid to 0, so we avoid recursions errors 
    # and repeating calls to dfs in the driver code
    grid[x][y] = 0
    
    # call dfs on all valid coordinates that are adjacent to where we are. Add their
    # acumalated are to our area
    if x > 0: area += dfs((x-1, y), grid)
    if y > 0: area += dfs((x, y-1), grid)
    if x+1 < len(grid): area += dfs((x + 1, y ), grid)
    if y+1 < len(grid[0]): area += dfs((x, y + 1 ), grid)
        
    return area
