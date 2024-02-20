# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.list = []
        self.traverse(root , "")
        result = 0
        if root is None:
            return None
        for num in self.list:
            result += int(num)
        return result
    
    def traverse(self , node , result):
        if node is not None:
            result += str(node.val)
            if node.left is None and node.right is None:
                self.list.append(result)
            else:
             self.traverse(node.left , result)
             self.traverse