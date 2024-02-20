class Solution:
    def divisorGame(self, n: int) -> bool:
        if n%2 == 0 :
          return True
        else:
          return False

test = Solution()
print(test.divisorGame(3))
print(test.divisorGame(2))