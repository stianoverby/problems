""" Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        start = ListNode(0)
        current = start
        carry = 0
        
        while l1 or l2 or carry:
            
            x = 0
            if l1: x = l1.val
                
            y = 0
            if l2: y = l2.val
                
            acc = carry + x + y
            
            carry = acc // 10
            current.next = ListNode(acc % 10)
            current = current.next
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return start.next
