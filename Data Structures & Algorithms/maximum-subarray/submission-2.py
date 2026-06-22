class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        runSum = 0
        maxSum = max(nums)
        for num in nums:
            runSum += num
            maxSum = max(runSum, maxSum)
            if runSum < 0:
                runSum = 0
                

        return maxSum