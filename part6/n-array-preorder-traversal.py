"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root):
      self.result = []
      if root == []:
        return None
      self._traverse_(root)
      return self.result

    def _traverse_(self , node):
      if node.children is not None:
        self.result.append(node.val)        
        while node.children is not None and  len(node.children) != 0:
         self._traverse_(node.children.pop(0))