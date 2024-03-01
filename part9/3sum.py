class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.nums = nums
        if nums is None:
            return None
        for i in range(len(nums)):
          self.traverse([nums[i]] , {i})
        print(self.result)
    

    def traverse(self , current_li , indx_set  ):
      if len(current_li) > 3:
        return
      cur_sum = self.return_sum(current_li)
      if cur_sum == True and len(current_li) == 3:
        current_li.sort()
        if current_li not in self.result :
         self.result.append(current_li)
        return
      for i in range(len(self.nums)):
        if i not in indx_set:
          indx_set.add(i)
          self.traverse(current_li + [self.nums[i]] , indx_set)

    def return_sum(self , li):
        result = 0
        for elem in li:
            result += elem
        return result == 0