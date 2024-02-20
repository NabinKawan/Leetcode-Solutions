# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.set = set()
        result = list(self.set)
        result = sorted(result)
        if len(result) <= 1:
          return -1
        else:
          return result[1]
    
    def _traverse_tree_(self ,node):
      if node is not None:
        self.set.add(node.val)
        self._traverse_tree_(node.left)
        self._traverse_tree_(node.right)