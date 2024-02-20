# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        status = self._check_traverse_(root.left , root.right)
        if status == None:
          return True
        else:
          return False
    
    def _check_traverse_(self , left_node , right_node):
      if left_node is not None and right_node is not None:
        if left_node.val == right_node.val:
          self._check_traverse_(right_node , left_node)
          self._check_traverse_(left_node , right_node)
        else:
          return False