# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
          return None
        self.target = root.val
        self.current = True
        status = self._traverse_(head)
        return self.current
    
    def _traverse_(self , node):
      if node is not None:
        self._traverse_(node.left)
        self._traverse_(node.right)
        if node.val != target:
          current = False
          return False