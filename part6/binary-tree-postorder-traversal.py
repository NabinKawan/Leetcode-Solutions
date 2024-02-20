class Solution:
    def postorderTraversal(self, root):
      self.result = []
      self._traverse_(root)
      return self.result
    
    def _traverse_(self , node):
      if node is not None:
        self._traverse_(node.left)
        self._traverse_(node.right)
        self.result.append(node.val)