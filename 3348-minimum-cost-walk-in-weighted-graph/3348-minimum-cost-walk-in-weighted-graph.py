class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        ID = (1 << 31) - 1  
        d = [ID] * n
        adj = [[] for _ in range(n)]
        deg = [0] * n

        for u, v, w in edges:
            d[u] &= w
            d[v] &= w
            deg[u] += 1
            deg[v] += 1
            adj[u].append(v)
            adj[v].append(u)
        parent = list(range(n))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        def union(x, y):
            rx, ry = find(x), find(y)
            if rx != ry:
                parent[ry] = rx
        for u, v, _ in edges:
            union(u, v)
        comp_mask = {}
        for i in range(n):
            r = find(i)
            if r not in comp_mask:
                comp_mask[r] = ID
            comp_mask[r] &= d[i]
        ans = []
        for s, t in query:
            if find(s) != find(t):
                ans.append(-1)
            else:
                ans.append(comp_mask[find(s)])
        return ans