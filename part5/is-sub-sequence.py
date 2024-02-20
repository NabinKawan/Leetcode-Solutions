class Solution:
    def isSubsequence(self, s , t):
      prev_indx = 0
      t = [t[i] for i in range(len(t))]
      for i in range(len(s)):
        if s[i] not in t:
          return False
        else:
          if prev_indx > t.index(s[i]) :
            return False
          else:
            prev_indx = t.index(s[i])
            t[prev_indx] = "__"
      return True



test = Solution()
#print(test.isSubsequence("abc","ahbgdc"))
#print(test.isSubsequence("acb","ahbgdc"))
print(test.isSubsequence("ab","baab"))
print(test.isSubsequence("aaaaaa","bbaaaa"))