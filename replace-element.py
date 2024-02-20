class Solution:
    def replaceElements(self, arr):
      result_arr = []
      for i in range(len(arr)-1):
        maximum_number = None
        for j in range(i+1 ,len(arr)):
          if maximum_number is None or maximum_number < arr[j]:
            maximum_number = arr[j]
        arr[i] = maximum_number
      arr[-1] = -1
      return arr


test = Solution()
test.replaceElements([17,18,5,4,6,1])