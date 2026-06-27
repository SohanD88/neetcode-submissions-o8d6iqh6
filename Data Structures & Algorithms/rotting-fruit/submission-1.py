class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #1. iterate through matrix
        #2. if cell is empty or fresh, pass
        #3. if cell has rotten fruit, run BFS
        #4. Every iteration of BFS, add 1
        #5. if rotten fruit is next to fresh fruit, turn it rotten and continue BFS
        #6. if rotten fruit has no fresh fruit next to it, return count and continue.
        #7. After the very last element in the array, we loop through the array once more to see
        #7cont. if there are any more fresh fruit. If so, return -1 else return count

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque()
        freshCnt = 0
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    freshCnt += 1
                if grid[i][j] == 2:
                    queue.append((i, j))


        while freshCnt > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for addR, addC in directions:
                    row, col = r + addR, c + addC

                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                        grid[row][col] = 2
                        queue.append((row, col))
                        freshCnt -= 1

            time +=1

        if freshCnt == 0:
            return time

        return -1


            


