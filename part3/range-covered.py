class Solution:
    def isCovered(self, ranges, left: int, right: int):
      self.list = []
      for item in ranges:
        for subitem in range(item[0] , item[1]+1):
          self.list.append(subitem)
      self.set = set(self.list)
      for i in range(left , right+1):
        if i not in self.set:
          return False
      return True

test = Solution()
print(test.isCovered([[1,2],[3,4],[5,6]],2,5))