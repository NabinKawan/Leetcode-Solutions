class Solution:
    def bitwiseComplement(self, n: int) -> int:
      if n == 0:
        return 1
      elif n == 1:
        return 0
      else:
       binary_number = self._convert_to_binary_(n)
       binary_compliment = self._find_binary_compliment_(binary_number)
       decimal_number = self._convert_to_decimal_(binary_compliment)
       return decimal_number
    
    def _convert_to_binary_(self , num):
      remainder = ''
      while num != 0 :
        remainder += str(num%2)
        num = num//2
      return remainder[::-1]
    
    def _find_binary_compliment_(self , num):
      num = str(num)
      compliment = ''
      for i in range(len(num)):
        if num[i] == '0':
          compliment += '1'
        else:
          compliment += '0'
      return compliment
    
    def _convert_to_decimal_(self , num):
      nums = str(num)
      nums = nums[::-1]
      decimal_number = 0 
      for i in range(len(nums)):
        current_num = int(nums[i]) * (2 ** i)
        decimal_number += current_num
      return decimal_number




test = Solution()
print(test.bitwiseComplement(10))