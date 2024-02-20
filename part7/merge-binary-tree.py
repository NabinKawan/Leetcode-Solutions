# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1 , root2):
      pass

    def _run_merge_(self ,root1 , root2):
      if root1 is not None or root2 is not  None:
        if root1 is not None and root2 is not None:
          root1.val += root2.val