# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p,q) -> bool:
      is_valid = self._validate_identical_(p,q)
      return is_valid


    def _validate_identical_(self , node1 , node2):
      if node1 is not None and node2 is not None:
       if node1.val == node2.val:
        left_valid  = self._validate_identical_(node1.left , node2.left)
        right_valid = self._validate_identical_(node1.right , node2.right)
        return left_valid and right_valid
       else:
        return False
      return node1 is None and node2 is None
        