# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current_node = head
        while current_node.next is not None:
          prev_node = current_node
          current_node = current_node.next

          if current_node.val == val:
            prev_node.next = current_node.next
        