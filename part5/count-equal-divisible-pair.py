class Solution:
    def countPairs(self, nums , k):
      count = 0
      for i in range(len(nums)):
        for j in range(i , len(nums)):
          if nums[i] == nums[j] and (i*j)%k == 0 and i<j:
            print(nums[i] , nums[j])
            count += 1
      return count


test = Solution()
print(test.countPairs([3,1,2,2,2,1,3],2))