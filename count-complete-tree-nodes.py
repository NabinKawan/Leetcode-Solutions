#Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root):
      self.nodes = [root]
      total_nodes = 0
      while self.nodes:
        current_node = self.nodes.pop()
        if current_node is not None:
          total_nodes += 1

          if current_node.left is not None:
            self.nodes.append(current_node.left)
          if current_node.right is not None:
            self.nodes.append(current_node.right)
      return total_nodes