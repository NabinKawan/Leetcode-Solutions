class Solution(object):
    def mySqrt(self, x):
        current_num = 1
        while current_num < x:
          if current_num * current_num == x:
            return current_num
          elif current_num * current_num > x:
            return current_num -1 
          current_num += 1

test = Solution()
print(test.mySqrt(4))