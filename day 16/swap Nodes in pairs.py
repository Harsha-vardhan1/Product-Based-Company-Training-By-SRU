# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        if(head==None or head.next==None):
            return head
        temp1=head.next
        while(temp and temp1):
            t=temp.val
            temp.val=temp1.val
            temp1.val=t
            temp=temp.next.next
            if(temp1.next!=None):
              temp1=temp1.next.next
        return head
