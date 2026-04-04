class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        finalArr = []
        nums.sort()
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            currArr = []
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1

                else:
                    currArr = [nums[i], nums[l], nums[r]]
                    if currArr not in finalArr:
                        finalArr.append(currArr)
                    l += 1
                    r -= 1

                

        return finalArr
                    



