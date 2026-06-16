class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                maxProf = max(prices[j] - prices[i], maxProf)

        return maxProf

        