class Solution:
    def uniqueOccurrences(self, arr):
      same_occur = []
      self.dict = {}
      for elem in arr:
        if elem in self.dict:
          self.dict[elem] += 1
        else:
          self.dict[elem] = 1
      for value in self.dict.values():
        if value in same_occur:
          return False
        else:
          same_occur.append(value)
      return True
        
test = Solution()
print(test.uniqueOccurrences([1,2,2,1,1,3]))
print(test.uniqueOccurrences([1,2]))