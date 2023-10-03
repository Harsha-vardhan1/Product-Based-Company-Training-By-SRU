'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
'''def pri(n):
    if n==0:
        return 0
    print(n)
    pri(n-1)
    print(n)
n=int(input())
pri(n)https://www.onlinegdb.com/#tab-stdin'''
'''def sum(n):
    if n==0:
        return 0
    return sum(n//10)+n%10
n=int(input())
print(sum(n))'''
'''s=input()
i=0
l=len(s)-1 
flag=0
while(i<l):
    if s[i]!=s[l]:
        print("Fasle")
        flag=1
        break
    i+=1 
    l-=1 
if flag==0:
    print("True")'''
'''def check(s,i,l):
    if check(s,i+1,l-1):
        return
    
s=input()
i=0 
l=-1
def check(s,i,l):'''
'''def check(s,f,l):
    if(f==-1 and l==len(s)):
        return True
    elif s[f]!=s[l]:
        return False
    return check(s,f-1,l+1)
s=input()
j=(len(s)//2)
if(j%2==0):
    print(check(s,j-1,j))
else:
    print(check(s,j-1,j+1))'''
'''def check(s,i,j):
    if(i<j):
        if s[i]!=s[j]:
            return False
        else:
            return check(s,i+1,j-1)
    return True
        
s=input()
i=0
j=len(s)-1
print(check(s,i,j))'''
'''def po2(n,j):
    if j==n:
        return True
    elif j>n:
        return False 
    return po2(n,j*2)
n=int(input())
print(po2(n,1))'''
n=int(input())
l=[]
for i in range(0,n):
    m=[]
    for j in range(0,n):
        a=int(input())
        m.append(a)
    l.append(m)
print(l)
        
    
    
    
        