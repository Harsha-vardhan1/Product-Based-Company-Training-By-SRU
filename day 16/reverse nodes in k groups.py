# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp=head
        while(temp!=None):
            l=[]
            c=0
            temp1=temp
            while(c<k and temp1):
                l.append(temp1.val)
                c+=1
                temp1=temp1.next
            if(c<k):
                break
            c=0
            while(c<k):
                c+=1
                temp.val=l.pop()
                temp=temp.next
        return head
        