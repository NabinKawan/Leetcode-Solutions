class Solution(object):
    def findComplement(self, num):
       # conversion to binary
       self.binary_representation = ''
       self.reversed_str = ''
       self.decimal_value = 0

       if num == 1 :
        return 0
       elif num == 0:
        return 1


       while(num >= 1):
        self.binary_representation += str(num%2)
        num = num//2
       self.binary_representation =  self.binary_representation[::-1]
       bianry = self.reverse_str(self.binary_representation)
       final_decimal_value = self.convert_to_decimal(bianry)
       return final_decimal_value

    
    def reverse_str(self , word):
        for item in word:
            if item == '0':
                self.reversed_str += '1'
            else:
                self.reversed_str += '0'
        return self.reversed_str
    
    def convert_to_decimal(self , num):
        i = 1
        for item in num:
            self.decimal_value +=  int(item) * 2**(len(num)-i)
            i += 1
        return self.decimal_value


Test = Solution()
print(Test.findComplement(5))
print(Test.findComplement(24))
print(Test.findComplement(0))
print(Test.findComplement(1))
print(Test.findComplement(2))