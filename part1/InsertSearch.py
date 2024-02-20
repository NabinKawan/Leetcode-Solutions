class Solution(object):
    def searchInsert(self, nums, target):
        low = 0
        high = len(nums)-1
        while low <= high:
          mid = (low+high)//2
          if nums[mid] == target:
            return mid
          elif nums[mid] > target:
            high = mid-1
          else:
            low = mid+1
        return low
        
test = Solution()
print(test.searchInsert([1,3,5,6],5))