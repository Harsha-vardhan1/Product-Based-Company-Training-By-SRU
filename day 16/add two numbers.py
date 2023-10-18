# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        print(753865680+798580876)
        num=0
        temp=l1
        zc=0
        while(temp!=None):
            if(temp.val==0):
                zc+=1
                temp=temp.next
            else:
                break
            
        temp=l1
        while(temp!=None):
           num=num*10+temp.val
           temp=temp.next
        print(num)
        rev1=0
        while(num>0):
            rev1=rev1*10+num%10
            num=num//10
        rev1=rev1*(10**zc)
        print(rev1)
        temp=l2
        zc=0
        while(temp!=None):
            if(temp.val==0):
                zc+=1
                temp=temp.next
            else:
                break
        temp=l2
        while(temp!=None):
            num=num*10+temp.val
            temp=temp.next
        rev2=0
        while(num>0):
          rev2=rev2*10+num%10
          num=num//10
        rev2=rev2*(10**zc)
        #print(rev2)
        res=rev1+rev2
        print(res)
        l=[]
        while(res>0):
            l.append(res%10)
            res=res//10

        temp=l1
        if(len(l)==0):
            l.append(0)
        i=0
        print(l)
        while(temp!=None):
            temp.val=l[i]
            print(l[i])
            i+=1
            prev=temp
            temp=temp.next
        if(i<=len(l)-1):
            while(i<len(l)):
                node=ListNode(l[i])
                print(l[i])
                i+=1
                prev.next=node
                prev=node

        return l1