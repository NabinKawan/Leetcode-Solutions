# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head):
      self.head = None
      self.tail = None

      self.odd = []
      self.even = []

      self.turn = 1

      current_node = head
      while current_node is not None:
        if self.turn == 1:
          self.odd.append(current_node)
        else:
          self.even.append(current_node)
        
        current_node = current_node.next
        self.toggle_turn()
      
      for node in self.odd:
        self.append_to_list(node)
      
      for node in self.even:
        self.append_to_list(node)
      
      return self.head
      
    
    def append_to_list(self , node):
      if self.head is None:
        self.head = node
        self.tail = self.head
      else:
        self.tail.next = node
        self.tail = node
      node.next = None


    def toggle_turn(self):
      if self.turn == 1:
        self.turn = 2
      else:
        self.turn = 1
