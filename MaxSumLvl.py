# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        self.sums = {}
        
        if root is None:
            return None

        self.traverse(root , 1)

        max_val = None
        max_lvl = None

        for key,value in self.sums.items():
            if value > max_val or max_val is None and max_lvl is None:
                max_lvl , max_val = key , value
        
        return max_lvl
        
    

    def traverse(self , node , current_lvl):
        if node is not None:
            if current_lvl in self.sums:
                self.sums[current_lvl] += node.val
            else:
                self.sums[current_lvl] = node.val
            self.traverse(node.left , current_lvl + 1)
            self.traverse(node.right , current_lvl + 1)
