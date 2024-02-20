class Solution:
    def countGoodSubstrings(self, s: str) -> int:
      if s is None:
        return None
      elif s == " ":
        return 0
      i = 0
      j = 0
      count = 0
      sub_set = set()
      while i < len(s) and j < len(s):
        if s[j] not in sub_set:
          sub_set.add(s[j])
          j += 1
        else:
          sub_set.remove(s[i])
          i+=1
        if len(sub_set) == 3:
          count += 1
      return count
        

test = Solution()
test.countGoodSubstrings("xyzzaz")
test.countGoodSubstrings("aababcabc")