class Solution(object):
    def smallestRangeII(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        
        result = nums[-1] - nums[0]

        left = nums[0] + k
        right = nums[-1] - k

        for i in range(n - 1):
            high = max(right, nums[i] + k)
            low = min(left, nums[i+1] - k)
            result = min(result, high - low)
        
        return result
