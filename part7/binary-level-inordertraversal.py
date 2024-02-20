# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
      self.result = []
      self.queue = [root]
      if root is None:
        return None
      self.result.append([root.val])

      while len(self.queue)!= 0:
        node = self.queue.pop(0)
        self._traverse_(node)
      
      return self.result
    
    def _traverse_(self , node):
      tmp_list = []
      if node is not None:
        if node.left is not None:
          tmp_list.append(node.left.val)
          self.queue.append(node.left)
        if node.right is not None:
          tmp_list.append(node.right.val)
          self.queue.append(node.right)
        if len(tmp_list) != 0:
         self.result.append(tmp_list)

    