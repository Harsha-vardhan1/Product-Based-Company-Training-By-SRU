# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''l=ListNode(10)
        l1=ListNode(9)
        l.next=l1
        temp=l
        while(temp):
            print(temp.val)
            temp=temp.next'''
        temp=head
        num=0
        while(temp):
             num=num*10+temp.val
             temp=temp.next  
        num=num*2
        l=ListNode(num%10)
        num=num//10
        while(num>0):
            l1=ListNode(num%10)
            l1.next=l
            l=l1
            num=num//10
        print(num)
        return l