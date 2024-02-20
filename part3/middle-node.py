# Definition for singly-linked list.
import math
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
      node_list = []
      current_node = head
      while current_node is not None:
        node_list.append(current_node)
        current_node = current_node.next
      if len(node_list) % 2 == 0:
        mid_index = (len(node_list)//2) 
      else:
        mid_index = len(node_list)//2 
      return node_list[mid_index]
        