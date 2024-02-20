#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        self.less_then = []
        self.greater_then = []
        self.head = None
        self.tail = None
        self.ref_value = x 

        if head is None:
          return None
        
        current_node = head
        while current_node is not None:

          if current_node.val < self.ref_value:
            self.less_then.append(current_node.val)
          else:
            self.greater_then.append(current_node.val)
          current_node = current_node.next
        

        while len(self.less_then) != 0:
          self.append_to_list(self.less_then.pop(0))
        

        while len(self.greater_then) != 0:
          self.append_to_list(self.greater_then.pop(0))
        
        self.tail.next = None

        return self.head

    def append_to_list(self , val):
      node = ListNode(val)
      if self.head is None:
        self.head = node
        self.tail = self.head
      else:
        self.tail.next = node
        self.tail = node
        
