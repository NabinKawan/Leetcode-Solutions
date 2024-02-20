# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head , k):
      if head is None:
        return None
      self.head = head
      for i in range(k):
        self._rotate_linked_list_()
      return self.head
    

    def _rotate_linked_list_(self):
      end_node = None
      dummy_node = ListNode(0 , self.head)
      current_node = self.head
      while current_node is not None:
        if current_node.next is not None:
         if current_node.next.next == None:
          tmp_node = current_node.next
          current_node.next = None
          tmp_node.next = self.head
          self.head = tmp_node
        current_node = current_node.next
