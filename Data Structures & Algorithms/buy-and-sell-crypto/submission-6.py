class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0

        if len(prices) <= 1:
            return 0

        l, r = 0, 1

        while l < len(prices) and r < len(prices):
            if prices[r] <= prices[l]:
                l = r
                r += 1
            else:
                maxProf = max(prices[r] - prices[l], maxProf)
                r += 1        

        return maxProf