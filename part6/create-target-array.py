class Solution:
    def createTargetArray(self, nums , index):
      result = []
      for i in range(len(index)):
        result.insert(index[i] , nums[i])
      return result