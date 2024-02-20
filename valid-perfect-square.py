class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        count = 1
        current_num = 1
        while current_num <= num:
          current_num = count * count
          if current_num == num:
            return True
          count += 1
        return False


test = Solution()
print(test.isPerfectSquare(16))
print(test.isPerfectSquare(14))
print(test.isPerfectSquare(1))