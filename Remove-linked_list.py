
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

class Solution:
    def removeElements(self, head , val: int):
      target_val = val
      self.head = head
      current_node = self.head

      while current_node.val == target_val:
        current_node = current_node.next
      self.head = current_node

      current_node = self.head


      while current_node is not None:
        prev_node = current_node
        current_node = current_node.next 
        if current_node != None and current_node.val == target_val:
          prev_node.next = current_node.next
      return self.head
    
    def _traverse_nodes_(self):
      self.results = []
      curent_node = self.head
      while curent_node is not None:
        self.results.append(curent_node.val)
        curent_node = curent_node.next
      print(self.results)
        


test = generate_linked_nodes(5)
test._append_node_(3)
test._append_node_(3)


test2 = Solution()
test2.removeElements(test.head , 0)
test2._traverse_nodes_()
    
