class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution:
    def addTwoNumbers(self, l1,l2):
      self.head = None
      number1 = self._traverse_node_(l1)
      number2 = self._traverse_node_(l2)
      number3 = int(number1[::-1]) + int(number2[::-1])
      number3 = str(number3)
      for i in range(len(number3)):
        node = ListNode(int(number3[i]))
        if self.head is None:
          self.head = node
        else:
          self._append_to_list(node)
      return self.head


    def _traverse_node_(self , node_head):
      final = ""
      current_node = node_head
      while current_node is not None:
        value = current_node.val
        final += str(value)
        current_node = current_node.next
      return final
    
    def _append_to_list(self , node):
      node.next = self.head
      self.head = node

        