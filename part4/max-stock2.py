class Solution:
    def maxProfit(self, prices):
      profit = None
      while profit is None and len(prices) != 1:
        max_day = max(prices)
        min_day = min(prices)
        if prices.index(max_day) > prices.index(min_day):
          profit = max_day - min_day
        else:
          prices.remove(max_day)
      if profit is None:
        return 0
      else:
       return profit



test = Solution()
print(test.maxProfit([7,1,5,3,6,4]))
print(test.maxProfit([7,6,4,3,1]))
print(test.maxProfit([2,4,1]))