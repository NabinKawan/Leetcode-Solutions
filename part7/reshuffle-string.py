class Solution:
    def restoreString(self, s: str, indices):
      result_str = ""
      for i in range(len(indices)):
        index = indices.index(i)
        result_str += s[index]
      return result_str

test = Solution()
test.restoreString("codeleet",[4,5,6,7,0,2,1,3])
