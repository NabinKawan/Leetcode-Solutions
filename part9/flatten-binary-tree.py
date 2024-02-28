# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root):
      self.list = []
      if root is None:
        return None 
      self.preorder_traverse(root)
      self.head = self.list[0]
      self.tail = head
      for node in self.list[1::]:
        self.tail.left = None 
        self.tail.right = node  
        self.tail = node
    


    def preorder_traverse(self , node):
      if node is not None:
        self.list.append(node)
        self.preorder_traverse(node.left)
        self.preorder_traverse(node.right)