class Solution:
    def maxPower(self, s):
      self.max = 1
      for i in range(len(s)):
        current = 1
        if i != len(s) -1:
         while s[i+1] == s[i]:
          current += 1
          i += 1
        if self.max < current:
          self.max = current 
      return self.max 


test = Solution()
print(test.maxPower("leetcode"))
print(test.maxPower("abbcccddddeeeeedcba"))