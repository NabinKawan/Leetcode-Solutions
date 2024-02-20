
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val        
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root):
      self.result = []
      self._preorder_traverse_(root)
      self.head = root
      current_node = root
      while len(self.result) != 0:
        num = self.result.pop(0)
        if current_node.right is not None:
          current_node.val = num
          current_node.left  = None
        else:
          node = TreeNode(num)
          current_node.right = node
        current_node = current_node.right

    
    
    def _preorder_traverse_(self , node):
      if node is not None:
       self.result.append(node.val)
       self._preorder_traverse_(node.left)
       self._preorder_traverse_(node.right)