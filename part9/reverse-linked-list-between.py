# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        self.list = []
        left -= 1
        right -=1

        self.head = None 
        self.tail = None

        if head is None or head.next is None:
          return head
        
        current_node = head 
        while current_node is not None:
          self.list.append(current_node)
          current_node = current_node.next
        
        between_nodes = self.list[left:right+1][::-1]

        self.result = self.list[:left] + between_nodes + self.list[right:]

        for node in self.result:
          self.link_to_list(node)
        
        self.tail.next = None 

        return self.head
    

    def link_to_list(self , node):
      if head is None:
        self.head = node 
        self.tail = self.head 
      else:
        self.tail.next = node 
        self.tail = node          



