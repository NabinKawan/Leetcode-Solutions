class Solution:
    def search(self, nums, target: int) -> int:
        low = 0
        high = len(nums)-1
        while low<=high :
          mid = ( low + high )//2
          if nums[mid] == target:
            return mid
          elif nums[mid] > target:
            high = mid - 1
          else:
            low = mid +  1
        return -1


test = Solution()
print(test.search([-1,0,3,5,9,12], 9))
print(test.search([-1,0,3,5,9,12], 13))