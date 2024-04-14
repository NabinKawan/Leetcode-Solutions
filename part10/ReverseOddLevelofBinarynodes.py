# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        
        self.dict = {}

        self.traverse(root , 0)

        for key,values in self.dict.items():
            
            if len(values) == 1:
                pass
            else:
                last_index = -1
                for i in range(len(values)//2):
                    values[i].val , values[last_index].val = values[last_index].val , values[i].val
                    last_index -= 1
        
        return root


    def traverse(self , node , current_lvl):
        if node is not None:
            if current_lvl %2 == 1:
             if current_lvl in self.dict:
                 self.dict[current_lvl].append(node)
             else:
                self.dict[current_lvl] = [node]
            
            self.traverse(node.left , current_lvl+1)
            self.traverse(node.right , current_lvl+1)
