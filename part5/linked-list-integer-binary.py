# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head):
        binary_num = ""
        current_node = head
        while current_node is not None:
          binary_num += str(current_node.val)
          current_node = current_node.next
        return self._convert_to_decimal_(binary_num)
    

    def _convert_to_decimal_(self , num):
      decimal_result = 0
      num = num[::-1]
      for i in range(len(num)):
        decimal_result += int(num[i]) * (2**i)
      return decimal_result

test = Solution()
print(test._convert_to_decimal_("101"))
