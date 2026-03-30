class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCount = 0

        for i in range(len(nums)):
            if nums[i] - 1 not in numSet:
                inc = 1
                while nums[i] + inc in numSet:
                    inc += 1
                maxCount = max(maxCount, inc)

            else:
                continue

        return maxCount
                
                