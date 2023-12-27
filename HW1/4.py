from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BFS(self, s):
        visited = [False] * (self.V)
        dist = [0] * (self.V)
        queue = deque()
        
        queue.append(s)
        visited[s] = True
        
        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if not visited[v]:
                    visited[v] = True
                    dist[v] = dist[u] + 1
                    queue.append(v)
                    
        return max(dist)

    def findDiameter(self):
        diameter = 0
        for i in range(self.V):
            diameter = max(diameter, self.BFS(i))
        return diameter

# Example Usage
g = Graph(6)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)

print("Diameter of the given graph is", g.findDiameter())
