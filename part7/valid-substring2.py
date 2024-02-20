class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring = None
        max = 0
        i = 0
        j = 0
        aplha_set = set()
        if s == "":
            return 0
        elif s == " ":
            return 1
        while i != len(s) and j != len(s):
          seq = s[i:j]
          if s[j] not in aplha_set:
            aplha_set.add(s[j])
            j += 1
            if len(aplha_set) > max:
              max = len(aplha_set)
          else:
            aplha_set.remove(s[i])
            i += 1
        print(aplha_set)
        return max

test = Solution()
test.lengthOfLongestSubstring("pwwkew")
        