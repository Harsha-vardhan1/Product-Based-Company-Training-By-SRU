class Harsha:
    def mp(self,n:int)->bool:
        for i in range(2,n):
            if n%i==0:
                return False
        rev=0
        while(n>0):
            rev=rev*10+n%10
            n=n//10
        for i in range(2,rev):
            if rev%i==0:
                return False
        return True
    def neon(self,n:int)->bool:
       if n<10 and n*n<10 and n==n*n:
           return True
       else:
           s=n*n
           s1=n
           c=0 
           while(1):
               r=s1 
               s1=0 
               while(r>0):
                   s1=s1+r%10 
                   r=r//10
               if s1<=9:
                   break
           while(1):
               r=s 
               s=0 
               while(r>0):
                   s=s+r%10 
                   r=r//10
               if s<=9:
                   break
           if s1==s:
            return True 
       return False
               
n=int(input())
s=Harsha()
print(s.mp(n))
print(s.neon(n))
class Me:
    def __init__(mango):
        print("Hai,hello")
    def __init__(mango,mango1):
        super().__init__
        print("Hai")
s=Me(100)
        
