'''/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include<math.h>
int main()
{
  int b=(int)(pow(2,3));
  printf("%d",b);
2 3 4 5 6
    return 0;
}'''
#l=list(map(int,input().split()))
#print(l)
#m=input().split()

#print(m)
l=list(map(int,input().split()))
res=[]
for i in range(0,len(l)):
    flag=0
    for j in range(0,len(l)):
        if(l[i]^l[j]==0 and i!=j):
            flag=1
            break
    if flag==0:
        res.append(l[i])
print(res)
n=len(l)
print(n*(n+1)//2-sum(l))
