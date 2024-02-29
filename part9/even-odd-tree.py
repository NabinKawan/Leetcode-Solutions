# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        self.max = None 
        self.check_lvl(root , 1)

        if root is None:
          return False
        
        self.bucket = [[] for i in range(self.max)]

        self.traverse(root , 0)

        for i in range(len(self.bucket)):
          status = None 
          if i == 0 :
            status = self.check_odd_cond(self.bucket[i])
          elif i % 2 == 1:
            status = self.check_even_cond(self.bucket[i])
          else:
            status = self.check_odd_cond(self.bucket[i])
          if status == False:
              print(f"false {i}")
              return False    

        return True
            

    

    def traverse(self , node , lvl):
      if node is not None:
        self.bucket[lvl].append(node.val)
        
        self.traverse(node.left , lvl + 1)
        self.traverse(node.right , lvl + 1)

    
    def check_lvl(self , node , lvl):
      if node is not None:
        if self.max is None or self.max < lvl:
          self.max = lvl
        self.check_lvl(node.left , lvl+1)
        self.check_lvl(node.right , lvl+1)
    

    def check_odd_cond(self , li):
      if len(set(li)) != len(li) :
        return False
      new_li = [elem for elem in li if elem % 2 == 1]
      if new_li != li:
        return False  
      new_li.sort()
      return new_li == li 
    

    def check_even_cond(self , li):
      if len(set(li)) != len(li) :
        return False
      new_li = [elem for elem in li if elem % 2 == 0]
      if new_li != li:
        return False  
      new_li.sort()
      new_li.reverse()
      return new_li == li 
