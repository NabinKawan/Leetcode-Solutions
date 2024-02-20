class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(t) == 1:
        if t == s:
          return False
      for i in range(len(t)):
          if t[i] not in s:
            return False
      return True