# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
      current_node = head
      value_list = []
      while current_node is not None:
        value_list.append(current_node.val)
        current_node = current_node.next
      return value_list == value_list[::-1]
