# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head):
      current_node = self.head
      while current_node is not None:
        prev_node = current_node
        current_node = current_node.next

        if current_node is not None:
          divisor = self._return_greatest_divisor(prev_node.val , current_node.val)
          node = ListNode(divisor)
          prev_node.next = node
          node.next = current_node
      return head

    def _return_greatest_divisor(self, num1 , num2):
      divisor = min(num1 , num2)
      while num1%divisor !=0 or num2%divisor !=0:
        divisor -= 1
      return divisor

test = Solution()
print(test._return_greatest_divisor(50,80))