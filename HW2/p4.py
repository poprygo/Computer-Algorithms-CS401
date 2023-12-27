class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        assert 1 <= n <= 5 * 10**4, "Size of nums is out of bounds"
        assert all(-10**9 <= num <= 10**9 for num in nums), "Nums contain values out of bounds"
        
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        return candidate

solution = Solution()
print(solution.majorityElement([3,2,3])) 
print(solution.majorityElement([2,2,1,1,1,2,2]))  
