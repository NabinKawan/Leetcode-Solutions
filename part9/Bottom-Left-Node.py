# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.max_lvl = None 
        self.max = None 
        if root is None:
          return None 
        self.traverse(root , 0)
        return self.max

    
    def traverse(self , node , cur_lvl):
      if node is not None:
        cur_lvl += 1
        if self.max_lvl is None or cur_lvl > self.max_lvl:
          self.max_lvl = cur_lvl 
          self.max = node.val 
        self.traverse(node.left , cur_lvl)
        self.traverse(node.right , cur_lvl)