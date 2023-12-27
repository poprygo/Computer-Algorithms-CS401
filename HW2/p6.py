class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        if n == 1:
            return 0

        visited = [False] * n
        dist = [float('inf')] * n
        dist[0] = 0
        cost = 0

        for _ in range(n):
            u = self.minDistance(dist, visited)
            visited[u] = True
            cost += dist[u]

            for v in range(n):
                if not visited[v]:
                    dist[v] = min(dist[v], manhattan(points[u], points[v]))

        return cost

    def minDistance(self, dist, visited):
        """Utility function to find the vertex with the minimum distance value, from the set of vertices not yet included in MST"""
        min_val = float('inf')
        min_index = -1
        for v in range(len(dist)):
            if dist[v] < min_val and not visited[v]:
                min_val = dist[v]
                min_index = v
        return min_index

solution = Solution()
print(solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))  # Output: 20
print(solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))  # Output: 18
