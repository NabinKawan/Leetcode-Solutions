# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        self.list = []
        curr_node = head 
        while curr_node is not None:
          if curr_node in self.list :
            return  curr_node
          else:
            self.list.append(curr_node)
          curr_node = curr_node.next 
        
        return None