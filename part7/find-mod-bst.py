# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root):
      self.dict = {}
      result = []
      max = 0
      if root is None:
        return None
      self._traverse_(root)
      for value in self.dict.values():
        if max < value:
          max = value
      for key ,value in self.dict.items():
        if value == result:
          result.append(key)
      return result
    
    
    def _traverse_(self , node):
      if node is not None:
        if node.val in self.dict:
          self.dict[node.val] += 1
        else:
          self.dict[node.val] = 1
        self._traverse_(node.left)
        self._traverse_(node.right)
        