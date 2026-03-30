class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Running count and check number of 0s
        prod = 1
        zeroCount = 0
        prodArr = len(nums) * [0]

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCount += 1
            else:
                prod = prod * nums[i]

        for i in range(len(nums)):
            if zeroCount > 1:
                prodArr[i] = 0
            elif zeroCount == 1:
                if nums[i] == 0:
                    prodArr[i] = prod
                else:
                    nums[i] = 0
            else:
                prodArr[i] = prod // nums[i]

        return prodArr

   
