class Solution:
    def addToArrayForm(self, num , k):
      num1 = 0
      final_list = []
      num.reverse()
      for i in range(len(num)):
        num1 += num[i] * (10**i)
      num2 = num1 + k 

test = Solution()
test.addToArrayForm([1,2,0,0],34)