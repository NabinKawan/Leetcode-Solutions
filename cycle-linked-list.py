
class Solution:
    def hasCycle(self, head):
      self.node_list = []
      current_node = head
      while current_node is not None:
        if current_node in self.node_list:
          return True
        else:
          self.node_list.append(current_node)
        current_node = current_node.next
      return False
        