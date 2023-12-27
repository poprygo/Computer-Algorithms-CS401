class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        assert 1 <= len(cost) <= 100, "Number of candies is out of bounds"
        assert all(1 <= candy <= 100 for candy in cost), "Candy cost is out of bounds"

        cost.sort(reverse=True)
        total_cost = 0

        i = 0
        while i < len(cost):
            if i < len(cost):
                total_cost += cost[i]
                i += 1
            if i < len(cost):
                total_cost += cost[i]
                i += 1
            i += 1  

        return total_cost

solution = Solution()
print(solution.minimumCost([1,2,3])) 
print(solution.minimumCost([6,5,7,9,2,2]))  
print(solution.minimumCost([5,5])) 
