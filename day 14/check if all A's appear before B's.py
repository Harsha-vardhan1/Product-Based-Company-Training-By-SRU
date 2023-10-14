class Solution:
    def checkString(self, s: str) -> bool:
        '''l=[]
        for c in s:
           if(c=='a'):
               l.append(0)
           else:
               if len(l)==0:
                   return False
               l.pop()
        if(len(l)==0):
          return True
        return False'''
        s1=""
        l=[]
        for c in s:
            if(c=='a'):
                l.append(0)
            else:
                l.append(1)
        if(sorted(l)==l):
            return True
        return False