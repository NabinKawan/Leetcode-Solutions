class Solution:
    def combinationSum(self, candidates , target):
      self.result = []
      self.target = target
      self.candidates = candidates
      self.candidates.sort()

      i = 0
      for elem in self.candidates:
        self.traverse([elem])
      return self.result
    
    def traverse(self , current_list):
      current_sum = self.return_sum(current_list)
      if current_sum > self.target:
        return
      elif current_sum == self.target:
        current_list.sort()
        if current_list not in self.result:
         self.result.append(current_list)
      else:
        for i in range(len(self.candidates)):
         self.traverse( current_list + [self.candidates[i]]  )


    def return_sum(self , arr):
      result = 0
      for elem in arr:
        result += elem
      return result

test = Solution()
print(test.combinationSum([2],1))