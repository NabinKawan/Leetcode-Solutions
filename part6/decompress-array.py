class Solution:
    def decompressRLElist(self, nums):
      result = []
      if nums == []:
        return none
      i = 0
      while len(nums) != 0:
        freq = nums.pop(0)
        num = nums.pop(0)
        for i in range(freq):
          result.append(num)
      return result

test = Solution()
print(test.decompressRLElist([1,2,3,4]))
print(test.decompressRLElist([65,44,72,15]))