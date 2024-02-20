# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
      self.result = []
      self._traverse_(root)
      return self.result
    
    def _traverse_(self , node):
      if node is not None:
        self._traverse_(node.left)
        self.result.append(node.val)
        self._traverse_(node.right)
        