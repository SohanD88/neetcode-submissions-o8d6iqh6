class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(row, col, vis, prev):
            if (
                (row, col) in vis or
                row < 0 or
                col < 0 or
                row == rows or
                col == cols or
                heights[row][col] < prev
            ):
                return

            vis.add((row, col))

            dfs(row + 1, col, vis, heights[row][col])
            dfs(row - 1, col, vis, heights[row][col])
            dfs(row, col + 1, vis, heights[row][col])
            dfs(row, col - 1, vis, heights[row][col])

        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    dfs(i, j, pacific, heights[i][j])

                if i == rows - 1 or j == cols - 1:
                    dfs(i, j, atlantic, heights[i][j])

        res = []

        for r, c in pacific:
            if (r, c) in atlantic:
                res.append([r, c])

        return res