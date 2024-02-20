class Solution(object): 
    def addDigits(self, num):
      final_digit_length = 11
      final_digit = 0
      while final_digit_length > 1:
        final_digit = 0
        num = str(num)
        for i in range(len(num)):
          final_digit +=  int(num[i])
        final_digit_length = len(str(final_digit))
        num = final_digit
      print(final_digit)



test = Solution()
test.addDigits(38)