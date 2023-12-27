class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        setB = set(bobSizes)
        
        for x in aliceSizes:
            y = x + (sumB - sumA) // 2
            if y in setB:
                return [x, y]
            
solution = Solution()
print(solution.fairCandySwap([1,1], [2,2]))
print(solution.fairCandySwap([1,2], [2,3]))
print(solution.fairCandySwap([2], [1,3]))