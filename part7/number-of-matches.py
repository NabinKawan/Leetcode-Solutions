class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n != 1:
          n = n//2
          matches += n//2
        print(matches)

test = Solution()
test.numberOfMatches(7)