class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = []
        mx = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > 0:
                    value = prices[j] - prices[i]
                    max_profit.append(value)
        if len(max_profit) != 0:
            for i in range(len(max_profit)):
                if mx < max_profit[i]:
                    mx = max_profit[i]
            return mx
        else:
            return 0
        

        