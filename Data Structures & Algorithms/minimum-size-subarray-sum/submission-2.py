class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSub = float("inf")
        runSum = 0
        l, r = 0, 0
        
        while r < len(nums):
            runSum += nums[r]
            
            while runSum >= target:
                minSub = min((r-l)+1, minSub)
                runSum -= nums[l]
                l += 1

            r += 1
            

        if minSub == float("inf"):
            return 0
        else:
            return minSub