class Solution:
    def greatestLetter(self, s):
      valid_letters = []
      for i in range(len(s)):
        if s[i].upper() in s and s[i].lower() in s:
          valid_letters.append(s[i])
      if len(valid_letters) == 0:
        return ""
      else:
       return max(valid_letters).upper()

test = Solution()
print(test.greatestLetter("lEeTcOdE"))
        