# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        self.low = low
        self.high = high
        self._traverse_bst_(root)
        return self.sum
    

    def _traverse_bst_(self ,node):
      if node is not None:
        if node.val >= self.low and node.val <= self.high:
          self.sum += node.val
        self._traverse_bst_(node.left)
        self._traverse_bst_(node.right)