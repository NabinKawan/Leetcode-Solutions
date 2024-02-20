class Solution:
    def subsetsWithDup(self, nums):
        result = []
        for i in range(2**len(nums)):
          binary = self.convert_to_biary(i , len(nums))
          tmp_list = []
          for j in range(len(binary)):
            if binary[j] == '1' :
              tmp_list.append(nums[j])
          tmp_list.sort()
          if tmp_list not in result:
           result.append(tmp_list)
        return result

    

    def convert_to_biary(self , num , max_bit):
      final = ""
      while num != 0:
        final = str(num%2) + final 
        num = num //2

      if len(final) != max_bit:
        final = "0"*(max_bit - len(final)) + final 
      return final






test = Solution()

print(test.subsetsWithDup([1,2,2]))

"""
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""