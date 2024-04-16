# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        self.target_lvl = depth-1
        self.val = val
        if root is None:
            return None
        if self.target_lvl == 0:
            new_node = TreeNode(self.val)
            new_node.left = root
            return new_node
        else:
            self.traverse(root , 1)

        return root

    def traverse(self , node , current_lvl):
        if node is not None:
            if current_lvl == self.target_lvl:
                left_node = TreeNode(self.val)
                right_node = TreeNode(self.val)
                
                left_node.left = node.left
                right_node.right = node.right

                node.left = left_node
                node.right = right_node
                return 

            self.traverse(node.left , current_lvl+1)
            self.traverse(node.right , current_lvl+1)
