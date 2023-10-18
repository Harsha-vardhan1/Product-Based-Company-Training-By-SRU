# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=0
        temp=head
        if(head.next==None):
            return None
        while(temp!=None):
            c+=1
            temp=temp.next
        print(c)
        if(n==c):
            head=head.next
            return head
        c1=0
        temp=head
        prev=head
        c1=0
        while(temp!=None):
            prev=temp
            c1+=1
            temp=temp.next
            if(c1==c-n):
                break
        if(temp==None):
            return head
        prev.next=temp.next
        return head
        