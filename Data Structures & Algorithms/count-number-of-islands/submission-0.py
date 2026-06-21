class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, row, col, seen):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                return False

            if grid[row][col] == "0":
                return False

            pos = (row, col)
            if pos in seen:
                return False

            seen.add(pos)

            dfs(grid, row - 1, col, seen)
            dfs(grid, row + 1, col, seen)
            dfs(grid, row, col - 1, seen)
            dfs(grid, row, col + 1, seen)

            return True

        seen = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if dfs(grid, i, j, seen) == True:
                    count += 1

        return count
