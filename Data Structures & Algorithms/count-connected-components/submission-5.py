class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        comp = {i : [] for i in range(n)}

        for u,v in edges:
            comp[u].append(v)
            comp[v].append(u)
        visit = [False] * n

        def dfs(node):
            #visist nodes and make them as true
            visit[node] = True

            for nei in comp[node]:
                if not visit[nei]:
                    dfs(nei)

        count = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                count += 1
                dfs(node)
        return count
