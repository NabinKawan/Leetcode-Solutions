# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):

        if root is None:
            return None

        self.p = p
        self.q = q

        self.first_node_ancestors = None
        self.second_node_ancestors = None

        self.traverse(root , [root])

        self.common = root

        for node in self.first_node_ancestors:
            if node in self.second_node_ancestors:
                self.common = node
        
        return self.common

    


    def traverse(self , node , nodes_list):
        if self.first_node_ancestors is None or self.second_node_ancestors is None:
            if node is not None:
                if node == self.p:
                    self.first_node_ancestors = nodes_list
                if node == self.q:
                    self.second_node_ancestors = nodes_list
                
                self.traverse(node.left , nodes_list + [node.left])
                self.traverse(node.right , nodes_list + [node.right])
