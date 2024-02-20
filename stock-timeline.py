class Solution(object):
    def maxProfit(self, prices):
      profit = []
      if len(prices) == 1:
        return 0
      for i in range(len(prices)):
        for j in range(i+1 , len(prices)):
          profit.append(prices[j]-prices[i])
      maximum_profit = list(reversed(sorted(profit)))
      if maximum_profit[0] > 0:
        return maximum_profit[0]
      else:
        return 0


test = Solution()
print(test.maxProfit([7,1,5,3,6,4]))
print(test.maxProfit([7,6,4,3,1]))

        