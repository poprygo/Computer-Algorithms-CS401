class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        assert 1 <= len(nums) <= 5000, "Length of nums is out of bounds"
        assert all(1 <= num <= 10**4 for num in nums), "Nums contain values out of bounds"

        ops = 0
        for i in range(1, len(nums)):
            while nums[i] <= nums[i-1]:
                nums[i] += 1
                ops += 1
        return ops

solution = Solution()

nums1 = [1,1,1]
print(solution.minOperations(nums1))  

nums2 = [1,5,2,4,1]
print(solution.minOperations(nums2)) 

nums3 = [8]
print(solution.minOperations(nums3))  
