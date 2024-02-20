class Solution:
    def findJudge(self, n , trust):
      candidate = trust[0][1]
      for item in trust:
        if candidate != item[1]:
          return -1
      else:
        return candidate


test = Solution()
print(test.findJudge(2,[1,2]))
print(test.findJudge(3,[[1,3],[2,3]]))