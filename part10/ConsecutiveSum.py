class Solution(object):
    def sumOfThree(self, num):
        
        num -= 3

        num = num/3.0

        if num%1 == 0:
            num = int(num)
            return [num , num+1 , num+2]
        else:
            return []
