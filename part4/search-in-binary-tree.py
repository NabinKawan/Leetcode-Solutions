# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        self.nodes_list = [root]
        target_node_vals = []
        result_val = []
        while len(self.nodes_list) != 0:
            current_node = self.nodes_list.pop()
            if current_node.val == val:
                result_val.append(current_node.val)
                target_node_vals.append(current_node)
                while len(target_node_vals) != 0:
                    current_node = target_node_vals.pop()
                    if current_node.left != None:
                        target_node_vals.append(current_node.left)
                        result_val.append(current_node.left.val)
                    if current_node.right != None:
                        target_node_vals.append(current_node.right)
                        result_val.append(current_node.right.val)
                return result_val
            if current_node.left != None:
                self.nodes_list.append(current_node.left)
            if current_node.right != None:
                self.nodes_list.append(current_node.right)
        return None
                
node1 = TreeNode(4)
node2 = TreeNode(2)
node3 = TreeNode(7)
node4 = TreeNode(1)
node5 = TreeNode(3)
node1.left = node2
node1.left.left = node4
node1.left.right = node5
node1.right = node3

test = Solution()
test.searchBST(node1 , 100)