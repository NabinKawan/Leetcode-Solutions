# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
      if head is None or head.next is None:
        return None        
      self.head = head
      current_node = head
      while current_node is not None:
        prev_node = current_node
        current_node = current_node.next
        if current.next is not None:
          if prev_node == self.head:
            prev_node.next , current_node.next = current_node.next , 
        