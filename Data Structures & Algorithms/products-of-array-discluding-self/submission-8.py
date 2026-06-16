class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodNoZero = 1
        outputArr = [0] * len(nums)
        zeroCount = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            else:
                prodNoZero *= nums[i]

        for i in range(len(nums)):
            if zeroCount > 1:
                return outputArr
            elif zeroCount == 1:
                if nums[i] == 0:
                    outputArr[i] = prodNoZero
                else:
                    outputArr[i] = 0
            else:
                outputArr[i] = prodNoZero // nums[i]

        return outputArr