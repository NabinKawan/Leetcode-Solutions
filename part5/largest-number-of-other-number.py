class Solution:
    def dominantIndex(self, nums):
      if nums is []:
        return -1
      max_num = max(nums)
      max_index = nums.index(max_num)
      nums.remove(max_num)
      second_max_num = max(nums)
      if max_num  >= second_max_num*2:
        return max_index
      else:
        return -1


test = Solution()
print(test.dominantIndex([3,6,1,0]))
print(test.dominantIndex([1,2,3,4]))