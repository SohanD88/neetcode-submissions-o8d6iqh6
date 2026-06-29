class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        def buildGraph():
            for i in range(n):
                graph[i] = []

            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)

        buildGraph()
        visited = set()

        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for nei in graph[node]:
                dfs(nei)

        count = 0

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)

        return count