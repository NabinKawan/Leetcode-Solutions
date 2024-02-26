class Solution:
    def combinationSum2(self, candidates , target):
        self.candidates = candidates
        self.result = []
        self.target = target
        for i in range(len(self.candidates)):
          self.traverse([i])
        
        return self.result

    
    def traverse(self , current_li):
      cur_sum = self.return_sum(current_li)
      if cur_sum > self.target:
        return
      elif cur_sum == self.target:
        li = [self.candidates[indx] for indx in current_li]
        li.sort()
        if li not in self.result:
         self.result.append(li)
      else:
        for i in range(len(self.candidates)):
          if i not in current_li:
            self.traverse(current_li + [i])
  

    def return_sum(self , li):
      result = 0
      for indx in li:
        result += self.candidates[indx]
      return result


test = Solution()
print(test.combinationSum2([10,1,2,7,6,1,5] , 8))