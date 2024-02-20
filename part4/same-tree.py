# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q):
      self.list1 = [p]
      self.result_tree_1 = [p.val]
      self.list2 = [q]
      self.result_tree_2 = [q.val]
      
      while self.list1:
        current_node = self.list1.pop()

        if current_node.left is not None:
          self.list1.append(current_node.left)
          if current_node.left.val is null:
            self.result_tree_1.append(-1)
          else:
            self.result_tree_1.append(current_node.left.val)
        
        if current_node.right is not None:
          self.list1.append(current_node.right)
          if current_node.right.val is null:
            self.result_tree_1.append(-1)
          else:
           self.result_tree_1.append(current_node.right.val)
      
      while self.list2:
        current_node = self.list2.pop()

        if current_node.left is not None:
          self.list2.append(current_node.left)
          if current_node.left.val is null:
            self.result_tree_2.append(-1)
          else:
            self.result_tree_2.append(current_node.left.val)
        
        if current_node.right is not None:
          self.list2.append(current_node.right)
          if current_node.right.val is null:
            self.result_tree_2.append(-1)
          else:
            self.result_tree_2.append(current_node.right.val)

      return self.result_tree_1 == self.result_tree_2
