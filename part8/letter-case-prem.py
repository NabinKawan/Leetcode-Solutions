class Solution:
    def letterCasePermutation(self, s):
        final = []
        for i in range(2**len(s)):
          binary = self.convert_to_binary(i , len(s))
          result = ""
          for j in range(len(binary)):
            if binary[j] == "1":
              result += s[j].upper()
            else:
              result += s[j].lower()
          if result not in final:
            final.append(result)
        return final


    
    def convert_to_binary(self , num , max_digit):
      result = ""
      while num != 0:
        result = str(num%2) + result
        num = num//2
      if len(result) != max_digit:
        result = '0' * (max_digit - len(result)) + result
      return result




test = Solution()
test.letterCasePermutation("a1b2")


print(test.convert_to_binary(3,3))


"""

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

"""