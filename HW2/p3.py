class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        assert 1 <= n <= 10**4, "Number of pairs is out of bounds"
        assert len(nums) == 2 * n, "Length of nums must be 2n"
        assert all(-10**4 <= num <= 10**4 for num in nums), "Nums contain values out of bounds"
        
        nums.sort()

        return sum(nums[::2])

solution = Solution()
print(solution.arrayPairSum([1,4,3,2]))  
print(solution.arrayPairSum([6,2,6,5,1,2]))  
