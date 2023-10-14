class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n=0
        for i in num:
            n=n*10+i
        n+=k
        l=[]
        while(n>0):
            l.append(n%10)
            n=n//10
        return l[::-1]
        