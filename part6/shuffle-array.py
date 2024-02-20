class Solution:
    def shuffle(self, nums ,n):
      list1 = nums[0:n]
      list2 = nums[n::]
      result = []
      for i in range(len(list1)):
        result.append(list1[i])
        result.append(list2[i])
      return result

test = Solution()
test.shuffle([2,5,1,3,4,7],3)