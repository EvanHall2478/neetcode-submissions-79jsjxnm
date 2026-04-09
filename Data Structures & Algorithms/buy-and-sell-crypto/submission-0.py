class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProf = 0 # Note: edge cases for whne max profit is negative

        while r < len(prices):
            maxProf = max((prices[r] - prices[l]), maxProf)
            if prices[r] < prices[l]: 
                l = r
                r = l + 1
            else:
                r += 1
        return maxProf