# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeElements(self, head, val: int):
      self.head = head
      value = val
      current_node = self.head
      while current_node is not None:
        prev_node = current_node
        current_node = current_node.next
        if prev_node.val == value:
          prev_node = current_node
          self.head = prev_node
        elif current_node != None and current_node.val == value:
          prev_node.next = current_node.next
          current_node = prev_node
      return self.head
    
def _traverse_node(x):
  current_node = x
  result = []
  while current_node is not None:
    result.append(current_node.val)
    current_node = current_node.next
  print(result)


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

test = Solution()

_traverse_node(node1)
node = test.removeElements( node1, 1)
_traverse_node(node)