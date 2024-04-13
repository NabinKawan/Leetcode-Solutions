# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        self.list = []

        self.traverse_tree(root1)
        self.traverse_tree(root2)

        self.list.sort()
        return self.list
    

    def traverse_tree(self , node):
        if node is not None:
            self.list.append(node.val)

            self.traverse_tree(node.left)
            self.traverse_tree(node.right)
