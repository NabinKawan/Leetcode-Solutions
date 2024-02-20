# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
      if head is None:
        return None
      dummy_node = head.next
      self._recur_swap(self.head)
      return dummy_node


    def _recur_swap(self , node):
      if node.next is not None:
        self._recur_swap(node.next)
        node , node.next = node , node.next     