class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        self.result = 0
        for num in nums:
          bits = self.convert_to_filtered_binary(num)
          if len(bits) == k :
            self.result += num 
        return self.result 
    


    def convert_to_filtered_binary(self , num):
      result = ""
      while num != 0:
        if num % 2 == 1:
          result += "1"
        num = num // 2
      return result