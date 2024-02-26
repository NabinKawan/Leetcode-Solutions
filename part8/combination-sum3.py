class Solution:
    def combinationSum3(self, k , n):
      self.result = []
      self.num_of_elems = k 
      self.target = n 
      for i in range(1, 10):
        self.traverse([i])
      return self.result


    def traverse(self , curr_list):
      total = self.return_total(curr_list)
      if len(curr_list) > self.num_of_elems or total > self.target:
        return
      elif len(curr_list) == self.num_of_elems and total == self.target:
        curr_list.sort()
        if curr_list not in self.result:
          self.result.append(curr_list)
        return 
      else:
        for i in range(1 ,10):
          if i not in curr_list:
            self.traverse(curr_list + [i])

    


    def return_total(self , li):
      result = 0
      for elem in li:
        result += elem
      return result


test = Solution()
test.combinationSum3(3,9)