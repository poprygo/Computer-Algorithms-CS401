from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, u, parent, number, low):
        number[u] = low[u] = self.time
        self.time += 1

        for v in self.graph[u]:
            if number[v] == -1:
                parent[v] = u
                self.DFS(v, parent, number, low)
                low[u] = min(low[u], low[v])
                if low[v] == number[v]:
                    print(f"{u} - {v} is a bridge")
            elif v != parent[u]:
                low[u] = min(low[u], number[v])

    def findBridges(self):
        V = len(self.graph)
        number = [-1] * V
        low = [float("Inf")] * V
        parent = [-1] * V

        for i in self.graph:
            if number[i] == -1:
                self.DFS(i, parent, number, low)

# Example Usage
g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(3, 4)

print("Bridges in the graph are:")
g.findBridges()
