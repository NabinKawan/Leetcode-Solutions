# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head , n ) :
      self.head = head
      self.list = []
      current_node = self.head
      while current_node is not None:
        self.list.append(current_node)
        current_node = current_node.next
      
      if self.list[-n] == self.head:
        self.head = self.list[-n].next
        return self.head
      elif n == 1 :
        self.list[-2].next = None
      else:
        self.list[-n-1].next = self.list[-n+1]
      return self.head
        