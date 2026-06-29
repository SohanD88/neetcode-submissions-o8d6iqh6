class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        
        while l < r:
            m = (l + r) // 2

           
            if nums[m] > nums[r]:
                l = m + 1
            # Otherwise, the minimum is in the left half (including m itself)
            else:
                r = m

        # When l == r, they point exactly to the minimum element value
        return nums[l]