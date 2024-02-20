# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
      self.head_node1 = list1
      self.head_node2 = list2
      self.final_node_head = None

      test_list = []

      while self.head_node1 != None:
        test_list.append(self.head_node1.val)
        self.head_node1 = self.head_node1.next
      
      while self.head_node2 != None:
        test_list.append(self.head_node2.val)
        self.head_node2 = self.head_node2.next
      
      test_list.sort(reverse=True)
      
      for items in test_list:
        self.convert_to_node(items)
      
      return self.final_node_head
    
    def convert_to_node(self , value):
      node = ListNode(value)
      if self.final_node_head is None:
        self.final_node_head = node
      else:
        node.next = self.final_node_head
        self.final_node_head = node

#[1,2,4] [1,3,4] [1,1,2,3,4,4]

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

test = Solution()
test.mergeTwoLists(node1 , node4)