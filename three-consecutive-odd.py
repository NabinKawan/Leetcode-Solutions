class Solution:
    def threeConsecutiveOdds(self, arr):
      self.arr = arr
      for i in range(len(self.arr)-2):
        if self.arr[i]%2 == 1:
          if self.arr[i+1]%2 == 1 and self.arr[i+2] % 2 == 1:
            return True
      return False

test = Solution()
print(test.threeConsecutiveOdds([2,6,4,1]))
print(test.threeConsecutiveOdds([1,2,34,3,4,5,7,23,12]))