# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        
        if head is None or head.next is None:
            return None

        self.list = []

        current_node = head

        while current_node is not None:
            self.list.append(current_node)

            current_node = current_node.next
        

        mid_node = len(self.list) // 2 

        if mid_node != len(self.list) - 1:
            self.list[mid_node - 1].next = self.list[mid_node].next
        else:
            self.list[mid_node -1 ].next = None
        
        return head
