# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        current_node = cloned
        self.node = self._traverse_node_(cloned , target)
    
    def _traverse_node_(node , target):
      if node is not None:
       if node.val == target.val:
        return node
       left_node =  self._traverse_node_(node.left)
       if left_node is not None:
        return left_node
       right_node = self._traverse_node_(node.right)
       if right_node is not None:
        return right_node