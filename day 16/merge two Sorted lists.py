# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
       temp2=list2
       temp1=list1
       temp=list1
       l=[]
       c=0
       prev=list1
       if(list1==None and list2==None):
           return None
       elif(list1!=None and list2==None):
           return list1
       elif(list1==None and list2!=None):
           return list2
       while(temp!=None):
           l.append(temp.val)
           c+=1
           prev=temp
           temp=temp.next
       end=temp
       prev.next=temp2
       i=0
       while(temp1!=None):
          if(i<c and temp2!=None and l[i]>temp2.val):
              temp1.val=temp2.val
              temp1=temp1.next
              temp2=temp2.next
          elif(i<c and temp2!=None):
              temp1.val=l[i]
              i+=1
              temp1=temp1.next
          elif(i<c):
              temp1.val=l[i]
              i+=1
              temp1=temp1.next
          else:
              temp1.val=temp2.val
              temp1=temp1.next
              temp2=temp2.next
       return list1