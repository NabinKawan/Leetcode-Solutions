class Solution:
    def grayCode(self, n):
        self.list = []
        result_list = []
        for i in range(2**n):
          self.list.append(self.convert_to_binary(i))
        for num in self.list:
          result = ""
          for i in range(len(num)):
            if i == 0:
              result += num[i]
            else:
              if num[i-1] != num[i]:
                result += "1"
              else:
                result += "0"
          result_list.append(result)
        final_list = []
        for num in result_list:
          final_list.append(self.convert_to_decimal(num))
        return final_list

    
    def convert_to_binary(self , num):
      result = ""
      while num != 0:
        result = str(num%2) + result
        num = num//2
      if result == "":
       return "0"
      return result
    
    def convert_to_decimal(self , num):
      num = num[::-1]
      result = 0
      for i in range(len(num)):
        result += int(num[i]) * (2 **i)
      return result


test = Solution()
print(test.grayCode(3))
test.convert_to_decimal("11")