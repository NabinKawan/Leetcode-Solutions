class Solution(object):
    def isPalindrome(self, x):
      self.x = str(x)
      reversed_str = ''
      for indx in reversed(range(0, len(self.x))):
        reversed_str += self.x[indx]

      if reversed_str == self.x:
        return True
      else:
        return False      


test1 = Solution()
test2 = Solution()
test3 = Solution()

print(test1.isPalindrome(121))
print(test2.isPalindrome(-121))
print(test3.isPalindrome(10))