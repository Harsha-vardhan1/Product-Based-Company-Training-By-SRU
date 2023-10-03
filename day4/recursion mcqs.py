'''Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.
'''
'''c=input()
if(ord(c)>=65 and ord(c)<=90):
    print(ord(c)-64)
elif(ord(c)>=97 and ord(c)<=122):
    print(ord(c)-96)'''
'''a=input()
k=int(input())
if(ord(a)-k-96<26):
    print(chr(ord(a)+k))
else:
    c=k-(122-ord(a))+97-26
    print(chr(c))
    print(ord(chr(c)))'''
'''n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print() '''
'''n=int(input())
for i in range(0,n):
    for j in range(0,2*n-1):
        if (i+j)>=n-1:
            print("*",end=" ")
        else:
            print(end=" ")
    print()'''
#n=int(input())
'''for i in range(n):
    print(" "*(n-i)+"* "*(i+1))
for i in range(n):
    print(" "*(i+1) + "* "*(n-i))'''
n=int(input())
for i in range(1,n+1):
     res=0
     j=i
     while j:
         res=res*10+i
         j-=1
     print(res)
     print((10**(i-1))*i)
     


