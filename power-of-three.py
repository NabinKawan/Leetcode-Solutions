class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
          return True
        current_number = 1
        while current_number <= n :
          current_number *= 3
          if current_number == n :
            return True
        return False



test = Solution()
print(test.isPowerOfThree(27))
print(test.isPowerOfThree(0))
print(test.isPowerOfThree(-1))