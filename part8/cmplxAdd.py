class Solution:
    def getSum(self, a: int, b: int) -> int:
       binary_a = self.convert_to_binary(a)
       binary_b = self.convert_to_binary(b)
       
       max_len = min(len(binary_a) , len(binary_b))

       final_binary = ""

       if len(binary_a) != max_len:
        binary_a = "0"*(max_len - len(binary_a)) + binary_a
       
       if len(binary_b) != max_len:
        binary_b = "0" *(max_len - len(binary_b)) + binary_b

       for i in range(max_len):
        if binary_a[i] == "0" and binary_b[i] == "0":
          final_binary += "1"
        elif binary_a[i] == "1" and binary_b[i] == "1":
          final_binary += "11"
        else:
          final_binary += "0"
      
        print(final_binary)


    def convert_to_binary(self , num):
        result = ""
        while num != 0:
            result = str(num%2) + result
            num = num //2
        return result


test = Solution()
test.getSum(2,2)