class Solution(object):
    def binaryTreePaths(self, root):
        if root is None:
            return []
        self.result = []
        self.traverse(root, str(root.val))
        return self.result
    
    def traverse(self, node, current_path):
        if node is not None:
            if node.left is None and node.right is None:
                self.result.append(current_path)
            if node.left:
                self.traverse(node.left, current_path + '->' + str(node.left.val))
            if node.right:
                self.traverse(node.right, current_path + '->' + str(node.right.val))
