# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1 , root2):
      self.seq1 = []
      self.seq2 = []
      self._traverse_(root1 , self.seq1)
      self._traverse_(root2  , self.seq2)
      return self.seq1 == self.seq2
    
    def _traverse_(node , li):
      if node is not None:
        if node.left is None and node.right is None:
          self.seq1.append(node.val)
        self._traverse_(node.left , li)
        self._traverse_(node.right ,li)