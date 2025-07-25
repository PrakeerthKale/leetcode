# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        current=dummy
        carry=0

        while l1 or l2 or carry:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0
            total=v1+v2+carry

            carry =total//10
            digit=total%10

            current.next=ListNode(digit)
            current=current.next

            if l1:
                l1=l1.next
            if l2:
                
                l2=l2.next
        return dummy.next
        