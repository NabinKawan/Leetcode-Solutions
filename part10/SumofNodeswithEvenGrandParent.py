# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        self.sum = 0
        self.traverse(root)
        return self.sum
    




    def traverse(self , node):
        if node is not None:
            if node.val % 2 == 0 and node.left is not None:
                if node.left.left is not None:
                    self.sum += node.left.left.val
                if node.left.right is not None:
                    self.sum += node.left.right.val
            if node.val%2 == 0 and node.right is not None:
                if node.right.left is not None:
                    self.sum += node.right.left.val
                if node.right.right is not None:
                    self.sum += node.right.right.val
            self.traverse(node.left)
            self.traverse(node.right)
