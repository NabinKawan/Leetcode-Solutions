class Solution:
    def duplicateZeros(self, arr):
      skip = False
      for i in range(len(arr)-1):
        if skip:
          skip = False
          pass
        elif arr[i] == 0:
          arr.insert(i+1 , 0)
          arr.pop()
          skip = True


test = Solution()
print(test.duplicateZeros([1,0,2,3,0,4,5,0]))