from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
            
        #Find the pivot
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        #Index of minimum element
        pivot = l
        
        #See which half the target is in
        if target <= nums[-1]:
            #Target is in right part
            l = pivot
            r = len(nums) - 1
        else:
            #Target is in left part
            l = 0
            r = pivot - 1

        #Binary Search on chosen part
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1