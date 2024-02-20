class Solution:
    def prefixCount(self, words , pref):
      num = 0
      for item in words:
        if item.startswith(pref):
          num += 1
      return num


test = Solution()
print(test.prefixCount(["pay","attention","practice","attend"],"at"))