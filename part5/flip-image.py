class Solution:
    def flipAndInvertImage(self, image):
      result_arr = []
      for arr in image:
        tmp = []
        for item in arr[::-1]:
          if item == 0:
            tmp.append(1)
          else:
            tmp.append(0)
        result_arr.append(tmp)
      return result_arr
      

test = Solution()
print(test.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))