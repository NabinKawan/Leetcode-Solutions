# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      self.list = []
      self.head = None 
      self.tail = None 
      if head is None:
        return None
      current_node = head 
      while current_node is not None:
          self.list.append(current_node.val)
          current_node = current_node.next
      self.list = list(filter(lambda x : self.appears_only_once(x) , self.list))
      if len(self.list) == 0:
          return None
      while len(self.list) != 0:
        val = self.list.pop(0)
        node = ListNode(val)
        if self.head is None:
          self.head = node
          self.tail = self.head
        else:
          self.tail.next = node
          self.tail = node
      self.tail.next = None
      return self.head
    
    def appears_only_once(self , num):
      freq = 0
      for item in self.list:
        if item == num:
          freq += 1
      return freq == 1
       
        