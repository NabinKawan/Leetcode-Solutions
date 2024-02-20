
class ListNode:
   def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class generate_linked_nodes:
  def __init__(self , n):
    self.n = n 
    self.head = None
    self.tail = None

    for i in range(n):
      self._append_node_(i)
    
  
  def _append_node_(self , x):
    node = ListNode(x)
    if self.head is None:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      self.tail = node
    

  
  def _traverse_node_(self):
    current_node = self.head
    result_list = []
    while current_node is not None:
      result_list.append(current_node.val)
      current_node = current_node.next
    print(result_list)


class Solution:
    def reverseList(self, head):
        current_node = head
        self.stack = []
        while current_node is not None:
          self.stack.append(current_node)
          current_node = current_node.next
        self.stack.reverse()
        self.head = None
        for i in range(len(self.stack)):
          if self.head is None:
            self.head = self.stack[i]
          try:
            self.stack[i].next = self.stack[i+1]
          except:
            self.stack[i].next = None
        return self.head

        



test = generate_linked_nodes(5)
test._traverse_node_()


test2 = Solution()
print(test2.reverseList(test.head))