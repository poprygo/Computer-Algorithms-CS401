class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        memo = {}
        
        def calculate(i, current_sum):
            if i == len(nums):
                return 1 if current_sum == target else 0
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]
            
            add = calculate(i + 1, current_sum + nums[i])
            subtract = calculate(i + 1, current_sum - nums[i])
            
            memo[(i, current_sum)] = add + subtract
            return memo[(i, current_sum)]
        
        return calculate(0, 0)

sol = Solution()
