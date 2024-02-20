class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        current_count = 0
        sum = 0
        dividend_is_negative = False
        diveser_is_negative = False
        if divisor < 0 :
          diveser_is_negative = True
          divisor = divisor * -1
        if dividend < 0 :
           dividend_is_negative = True
           dividend = dividend *-1
        while sum <= dividend:
          sum += divisor
          if sum <= dividend:
           current_count += 1
        if dividend_is_negative and diveser_is_negative:
          return current_count
        elif diveser_is_negative or dividend_is_negative:
          return current_count * -1
        else:
          return current_count



test = Solution()
print(test.divide(10 ,3))
print(test.divide(7 , -3))
print(test.divide(-1 , -1))