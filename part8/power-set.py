class Solution:
    def subsets(self, nums):
      nums_len = len(nums)
      result = []
      for i in range(2**nums_len):
        binary_num = self.return_binary_equivalent(i , nums_len)
        tmp_list = []
        for j in range(len(binary_num)):
          if binary_num[j] == "1":
            tmp_list.append(nums[j])
        result.append(tmp_list)
      return result

    def return_binary_equivalent(self , num , max_bit):
      final = "" 
      while num != 0:
        final = str(num%2) + final
        num = num//2
      if len(final) != max_bit:
        to_add = '0' * (max_bit - len(final))
        final = to_add + final
      return final





test = Solution()
print(test.subsets([1,2,3]))



"""
[1,2,3]
[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""