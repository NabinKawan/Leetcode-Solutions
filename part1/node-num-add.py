# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        self.str1 = self.traverse_node(l1)
        self.str2 = self.traverse_node(l2)
        self.result_node_head = None

        numA = int(self.str1[::-1])
        numB = int(self.str2[::-1])
        numC = str(numA + numB)
        self.handle_str_to_node(numC)
        return self.result_node_head.val
    
    def convert_to_node(self, i):
      node = ListNode(int(i))
      if self.result_node_head is None:
        self.result_node_head = node
      else:
        node.next = self.result_node_head
        self.result_node_head = node
    
    def handle_str_to_node(self , userStr):
      for i in range(len(userStr)):
        self.convert_to_node(userStr[i])


    def traverse_node(self, node):
        current_node = node
        blank_str = ''
        while current_node != None:
            blank_str += str(current_node.val)
            current_node = current_node.next
        return blank_str


test = Solution()
# print(test.addTwoNumbers([0],[0]))
# print(test.addTwoNumbers([9,9,9,9,9,9,9],[[9,9,9,9]]))

node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

print(test.addTwoNumbers(node1, node4))


node10 = ListNode(0)
node12 = ListNode(0)
print(test.addTwoNumbers(node10, node12))
