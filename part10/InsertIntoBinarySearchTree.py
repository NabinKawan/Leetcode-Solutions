# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        if root is None:
            root = TreeNode(val)
            return root
        self.append_to_bst(root , val)
        return root


    def append_to_bst(self , current_node , val):
        if current_node is not None:
            if current_node.left is None and val < current_node.val:
                current_node.left = TreeNode(val)
                return 
            if current_node.right is None and val > current_node.val:
                current_node.right = TreeNode(val)
                return 
            
            if val < current_node.val:
                self.append_to_bst(current_node.left , val)
            if val > current_node.val:
                self.append_to_bst(current_node.right , val)

        
