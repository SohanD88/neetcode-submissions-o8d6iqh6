class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        ROWS, COLS = len(board), len(board[0])
        visited = set()
        all_Os = []

        def dfs(r, c):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] == "X" or
                (r, c) in visited
            ):
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    all_Os.append((i, j))

                    if i == 0 or j == 0 or i == ROWS - 1 or j == COLS - 1:
                        dfs(i, j)

        for r, c in all_Os:
            if (r, c) not in visited:
                board[r][c] = "X"