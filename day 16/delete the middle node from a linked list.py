# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        temp1=head
        prev=head
        if(head.next==None):
            return None
        while(temp1 and temp1.next):
            prev=temp
            temp=temp.next
            temp1=temp1.next.next
        prev.next=temp.next
        return head
        
        