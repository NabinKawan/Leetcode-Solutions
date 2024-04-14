# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):

        if root is None:
            return None
        
        self.dict = {}

        self.traverse(root , 1)
        self.result = []

        for values in self.dict.values():
            self.result.append(sum(values)/float(len(values)))
        
        return self.result


    
    def traverse(self , node , current_lvl):
        if node is not None:
            if current_lvl in self.dict:
                self.dict[current_lvl].append(node.val)
            else:
                self.dict[current_lvl] = [node.val]
            
            self.traverse(node.left , current_lvl+1)
            self.traverse(node.right , current_lvl+1)
