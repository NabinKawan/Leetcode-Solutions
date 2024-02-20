# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
      self.list = []
      if head is None : return head
      self.head = None
      self.tail = None
      cur_node = head
      while cur_node is not None:
        self.list.append(cur_node.val)
        cur_node.next
      self.list.sort() 
      while len(self.list) != 0 :
        self.add_to_list(self.list.pop(0))
      self.tail.next = None
      return self.head
    

    def add_to_list(self , val):
      node = ListNode(val)
      if self.head is None:
        self.head = node
        self.tail = self.head
      else:
        self.tail.next = node
        self.tail = node