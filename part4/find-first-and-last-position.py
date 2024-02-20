class Solution:
    def searchRange(self, nums, target: int):
      initial_position = None
      last_position = None
      for i in range(len(nums)):
        if nums[i] == target:
          initial_position = i
          last_position = i
          j = 1
          try:
           while nums[i+1] == nums[i]:
             i+=1
             last_position = i
          except:
            pass
          return [initial_position , last_position]
      return [-1 , -1]

test = Solution()

print(test.searchRange([5,7,7,8,8,10],8))
print(test.searchRange([1],1))

        