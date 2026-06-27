class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen = set()
        queue = collections.deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append([i, j])
                    seen.add((i, j))
        distance = 0
        while queue:
            for i in range(len(queue)):
                row, col = queue.popleft()

                for addR, addC in directions:
                    r, c = row + addR, col + addC
                    if r < 0 or c < 0 or r >= len(grid) or c>=len(grid[0]) or (r, c) in seen or grid[r][c] == -1:
                        continue 
                    grid[r][c] = distance + 1
                    seen.add((r, c))
                    queue.append([r, c])


            distance += 1



                

                