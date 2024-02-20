class Solution:
    def canThreePartsEqualSum(self, arr) -> bool:
      sum = 0
      self.target_sum = 0
      self.stack = []
      for i in arr:
          sum += i
      self.target_sum = sum/3
      for value in arr:
        self._append_to_stack(value)
      return self.stack == []

    def _append_to_stack(self , value):
      final_sum = value
      for item in self.stack:
        final_sum += item
      if final_sum == self.target_sum:
        self.stack = []
      else:
        self.stack.append(value)

      


test = Solution()
print(test.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))
print(test.canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]))
print(test.canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]))