# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.list = []
        if root is None:
          return None
        self.list = sorted(self.list)
        return self.list[k-1]
    

    def _traverse_(self , node):
      if node is not None:
        self.list.append(node.val)
        self._traverse_(node.left)
        self._traverse_(node.right)