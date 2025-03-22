class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root_parent1 = self.find(node1)
        root_parent2 = self.find(node2)
        if root_parent1 == root_parent2:
            return
        if self.size[root_parent1] > self.size[root_parent2]:
            self.parent[root_parent2] = root_parent1
            self.size[root_parent1] += self.size[root_parent2]
        else:
            self.parent[root_parent1] = root_parent2
            self.size[root_parent2] += self.size[root_parent1]

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        edge_count = {}
        for u, v in edges:
            dsu.union(u, v)
        for u, v in edges:
            root = dsu.find(u)
            edge_count[root] = edge_count.get(root, 0) + 1
        complete_count = 0
        for vertex in range(n):
            if dsu.find(vertex) == vertex:
                node_count = dsu.size[vertex]
                expected_edges = (node_count * (node_count - 1)) // 2
                if edge_count.get(vertex, 0) == expected_edges:
                    complete_count += 1
        return complete_count
