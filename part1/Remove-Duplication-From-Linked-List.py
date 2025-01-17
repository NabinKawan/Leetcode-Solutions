# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        current_node = head
        self.head = head
        while current_node is not None:
          while current_node.next is not None and current_node.val == current_node.next.val:
            current_node.next = current_node.next.next
          current_node = current_node.next
        return self.head
        