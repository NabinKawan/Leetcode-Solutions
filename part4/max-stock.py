class Solution:
    def maxProfit(self, prices):
      profits = []
      for i in range(len(prices)):
        max_day = max(prices[i:len(prices)])
        profits.append(max_day - prices[i])
      max_profit = max(profits)
      if max_profit > 0:
        return max_profit
      else:
        return 0


test = Solution()
test.maxProfit([7,1,5,3,6,4])
print(test.maxProfit([7,6,4,3,1]))