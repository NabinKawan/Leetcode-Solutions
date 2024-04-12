# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        if a == 0:
            tail_of_list2 = self.return_tail(list2)
            self.join_node(tail_of_list2 , list1)
            return list2

        if list1 == None:
         return None
        
        current_node_index  = 0 
        partation_first_node = None
        partation_second_nod = None

        current_node = list1
        while True:
            if current_node.next is not None:
                if current_node_index + 1 == a:
                    partation_first_node = current_node
                if current_node_index == b :
                    paration_second_node = current_node.next
                    break
            current_node = current_node.next
            current_node_index += 1
        
        partation_first_node.next = list2

        tail_of_list2 = self.return_tail(list1)

        tail_of_list2.next = paration_second_node

        return list1


    def join_node(self , nodeA , nodeB):
        nodeA.next = nodeB

    def return_tail(self ,node):
        current_node = node
        while current_node.next is not None:
            current_node = current_node.next
        return current_node
