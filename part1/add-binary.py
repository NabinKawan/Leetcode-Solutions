class Solution(object):
    def addBinary(self, a, b):
      if a == "0" and b == "0" :
        return "0"


      NumA = self.binary_to_decimal(a)
      NumB = self.binary_to_decimal(b)
      Numc = self.decimal_to_binary(NumA+NumB)
      return str(Numc)

    def binary_to_decimal(self , strNum):
      final_num = 0
      strNum = strNum[::-1]
      for i in range(len(strNum)):
        final_num += int(strNum[i]) * (2**i)
      return final_num
    
    def decimal_to_binary(self , strNum):
      final_num = ''
      while strNum != 0:
        remainder = strNum%2
        strNum = strNum//2
        final_num += str(remainder)
      return final_num[::-1]


test = Solution()
print(test.addBinary("11","1"))


