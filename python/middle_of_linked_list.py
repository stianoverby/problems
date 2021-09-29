'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100

Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
  self.val = val
  self.next = next
  
'''
class Solution:
  
    '''
    Slow and fast pointer approach. Increase fast pointer at doubble the speed.
    '''
    def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow_pointer = slow_pointer = head
        
        while slow_pointer and fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        return slow_pointer
        
        
   '''
   Append to list and retrive element from middle index.
   '''     
   def middle_node(self, head: Optional[ListNode]) -> Optional[ListNode]:     
        Adding to list approach. Traverse the list and add nodes to list. Middle at
        index len(nodes)//2.
        
        nodes = [];
        traversing_node = head;
        
        while traversing_node != None:
            nodes.append(traversing_node)
            traversing_node = traversing_node.next
        
        return nodes[len(nodes)//2]
        
        
        
