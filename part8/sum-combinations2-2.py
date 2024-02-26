class Solution:
    def combinationSum2(self, candidates , target):
        self.candidates = candidates
        self.result = []
        self.target = target
        for i in range(len(self.candidates)):
          tmp_arr = list(filter( lambda candidate : candidate != self.candidates[i] , self.candidates ))
          self.traverse(tmp_arr)
        return self.result
    

    def traverse(self , curr_arr):
      total = self.return_total(curr_arr)
      if total < self.target:
        return
      elif total == self.target:
        curr_arr.sort()
        if curr_arr not in self.result:
         self.result.append(curr_arr)
        return
      else:
        for j in range(len(curr_arr)):
          sub_tmp_arr = curr_arr.copy()
          sub_tmp_arr.pop(j)
          self.traverse(sub_tmp_arr)


    def return_total(self , li):
      result = 0
      for elem in li:
        result += elem
      return result 
      



test = Solution()
test.combinationSum2([10,1,2,7,6,1,5] , 8)
test.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
27 )