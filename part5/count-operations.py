class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations = 0
        while num1 != 0 and num2 != 0:
          if num1 < num2:
            num2 -= num1
            operations += 1
          if num2 <= num1:
            num1 -= num2
            operations += 1
        return operations

test = Solution()
print(test.countOperations(2,3))