# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
      self.sum = 0
      self._traverse_node_(root)
      return self.sum
    
    def _traverse_node_(self , node , left_node = False):
      if node is not None:
        if node.left is None and node.right is None:
          if left_node:
            self.sum += node.val
        self._traverse_node_(node.left , True)
        self._traverse_node_(node.right , False)
