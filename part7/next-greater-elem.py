class Solution:
    def nextGreaterElement(self, nums1 , num2):
      result = []
      for num in nums1:
        if num in nums2:
          index = num2.index(num)
          inserted = false
          for i in range(index , len(num2)):
            if num2[i] < num:
              result.append(num2[i])
              inserted = True
          if not inserted:
            result.append(-1)
      return result