'''haystack = "sadbutsad"
needle = "but"

if needle in haystack:
  print(haystack.find(needle))
  print("exists")'''


class Solution(object):
      def strStr(self, haystack, needle):
          return haystack.find(needle)


test = Solution()
print(test.strStr("good","bad"))