# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        if head is None:
            return None
        if head.next is None:
            return head
        
        self.nodes = []
        
        current_node = head
        while current_node is not None:
            self.nodes.append(current_node)
            current_node = current_node.next
        
        self.nodes[k-1].val , self.nodes[-k].val = self.nodes[-k].val , self.nodes[k-1].val

        return head
