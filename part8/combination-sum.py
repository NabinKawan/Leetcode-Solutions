class Solution:
    def combinationSum(self, candidates , target):
     result = []
     for i in range(2**len(candidates)):
      tmp_list = []
      binary = self.convert_to_binary(i , len(candidates))
      for j in range(len(binary)):
        if binary[j] == "1":
          tmp_list.append(candidates[j])
      target_sum = 0
      for elem in tmp_list:
        target_sum += elem
      print(f"{target_sum} ------- {binary} ------- {tmp_list}")
      if target_sum == target: 
        result.append(tmp_list)
     return result 


    def convert_to_binary(self , num , max_digit):
      final = ""
      while num != 0:
        final = str(num%2) + final 
        num = num // 2
      if len(final) != max_digit:
        final = '0'*(max_digit - len(final)) + final
      return final
 





test = Solution()
test.convert_to_binary(3,3) 
print(test.combinationSum([2,3,6,7] , 7))



"""
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
"""