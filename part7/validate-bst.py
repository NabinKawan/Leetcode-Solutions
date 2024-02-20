# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
       self.leftsubtree = []
       self.rightsubtree =[]
       self._traverse_(root.left , self.leftsubtree)
       self._traverse_(root.right , self.rightsubtree)
       for num in self.leftsubtree:
        if num >= root.val:
          return False
       for num in self.rightsubtree:
        if num <= root.val:
          return False
    
    def _traverse_(self , node , subtree):
      if node is not None:
        subtree.append(node.val)
        self._traverse_(node.left , subtree)
        self._traverse_(node.right , subtree)