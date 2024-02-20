class Solution:
    def longestPalindrome(self, s: str):
      if s is None:
        return None
      i = 0
      j = 0
      longest_word = None
      while i != len(s) and j != len(s):
        seq = s[i:j]
        valid = self._is_valid_(seq)
        if valid :
          if longest_word is None or len(longest_word) > len(seq):
            longest_word = seq
            j +=1
        else:
          i+=1
      return longest_word
      
    def _is_valid_(self , s):
      return s == s[::-1]

test = Solution()
test.longestPalindrome("babad")