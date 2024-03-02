# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
          return head
        
        self.list = []

        current_node = head 

        while current_node is not None:
          self.list.append(current_node)
          current_node = current_node.next
        
        i = 0

        while i < len(self.list):
          
          if i + 1 < len(self.list):
           self.list[i] , self.list[i+1] = self.list[i+1] , self.list[i]

          i += 2
        

          self.head = None 
        self.tail = None 

        for node in self.list:
          print(node.val)
          self.append_to_list(node)
        
        self.tail.next = None 

        return self.head
      
    
    def append_to_list(self , node):
      if self.head is None:
        self.head = node 
        self.tail = self.head 
      else:
        self.tail.next = node
        self.tail = node

        
        