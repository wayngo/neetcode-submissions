class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = {i:[] for i in range(n)}

        visit = [False] * n
        for u,v in edges:
            connections[u].append(v)
            connections[v].append(u)
        
        def dfs(node):
            for nei in connections[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
        count = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                count += 1
                dfs(node)
        return count