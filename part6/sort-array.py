class Solution:
    def sortArrayByParityII(self, nums):
      odds = [num for num in nums if num%2 == 1]
      evens = [num for num in nums if num%2 == 0]
      result = []
      while len(odds) != 0 or len(evens) != 0:
        if len(evens) != 0:
          item = evens.pop()
          result.append(item)
        if len(odds) != 0:
          item = odds.pop()
          result.append(item)
      return result


test = Solution()
test.sortArrayByParityII([4,2,5,7])