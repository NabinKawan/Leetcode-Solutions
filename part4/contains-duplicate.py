class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        self.k = k
        status = False
        for i in range(len(nums)):
          for j in range(len(nums)):
            if nums[i] == nums[j]:
              if i - j <= self.k:
                status = True
              else:
                status = False
        return status