"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):

        if root is None:
            return None
        
        self.nodes_store = {}

        self.traverse(root , 1)

        self.result = [value for value in self.nodes_store.values()]

        return self.result


    
    def traverse(self , node , current_lvl):
        if node is not None:

            if current_lvl in self.nodes_store:
                self.nodes_store[current_lvl].append(node.val)
            else:
                self.nodes_store[current_lvl] = [node.val]
            
            for child in node.children:
                self.traverse(child , current_lvl + 1)
