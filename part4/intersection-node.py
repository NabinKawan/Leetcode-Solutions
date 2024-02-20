# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
      list1 = []
      current_node = headA
      while current_node is not None:
        list1.append(current_node)
        current_node = current_node.next
      current_node = headB
      while current_node is not None:
        if current_node in list1:
          return current_node
        current_node = current_node.next
      return None