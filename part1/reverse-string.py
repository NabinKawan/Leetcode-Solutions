class Solution(object):
    def reverseString(self, s):
      j = -1
      for i in range(len(s)//2):
        s[i] , s[j] = s[j] , s[i]
        j -= 1


test = Solution()
test.reverseString(["h","e","y"])
        