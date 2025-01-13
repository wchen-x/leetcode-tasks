class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans = [] 
        for i in range(len(nums)):
            x = target - nums[i]
            if x in nums and nums.index(x) != i:
                ans.append(i)
                ans.append(nums.index(x))
                break
        return ans

def main():
    solution = Solution()
    
    nums = [2, 7, 11, 15]
    target = 9
    
    result = solution.twoSum(nums, target)
    print("Result:", result)  # Expected output: [0, 1]

    nums = [3,2,4]
    target = 6
    
    result = solution.twoSum(nums, target)
    print("Result:", result)  # Expected output: [1, 2]
    
    nums = [3,3]
    target = 6
    
    result = solution.twoSum(nums, target)
    print("Result:", result)  # Expected output: [0, 1]
    
if __name__ == "__main__":
    main()