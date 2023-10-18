# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
       temp=head
       if(head==None):
            return head
       temp1=head
       t=head.val
       prev=head
       while(temp1!=None):
           prev=temp
           temp.val=t
           temp=temp.next
           while(temp1.val==t):
               temp1=temp1.next
               if(temp1==None):
                   break
           if(temp1==None):
               break
           t=temp1.val
       prev.next=None
       return head
