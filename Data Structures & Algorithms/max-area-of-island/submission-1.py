class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        def dfs(grid, r, c, seen):
            count = 0
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return 0

           
            if grid[r][c] == 0:
                return 0
            
            pos = (r,c)
            if pos in seen:
                return count
            
            seen.add(pos)

            count += 1
            count += dfs(grid, r - 1, c, seen)
            count += dfs(grid, r + 1, c, seen)
            count += dfs(grid, r, c - 1, seen)
            count += dfs(grid, r, c + 1, seen)

            return count


        maxArea = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                maxArea = max(maxArea, dfs(grid, i, j, seen))

        return maxArea