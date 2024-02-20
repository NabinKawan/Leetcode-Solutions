class Solution:
    def findErrorNums(self, nums):
      duplicated_num = 0
      new_li = []
      for i in range(len(nums)):
        if nums[i] in new_li:
          duplicated_num = nums[i]
        else:
          new_li.append(nums[i])
      nums_set = set(nums)
      missing_num = 0
      for i in range(1,len(nums)+1):
        if i not in nums_set:
          missing_num = i
          break
      
      new_list = []
      new_list.append(duplicated_num)
      new_list.append(missing_num)
      return new_list


test = Solution()
print(test.findErrorNums([1,2,2,4]))