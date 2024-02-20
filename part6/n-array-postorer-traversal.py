"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root):
      if root is None:
        return None
      self.list = []
      self._traverse_(root)
      return self.list
    
    def _traverse_(self , node):
      if node is not None:
        while node.children is not None and len(node.children) > 0: 
          self._traverse_(node.children.pop(0))
        self.list.append(node.val)