/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include<math.h>
int main()
{
  /*int n;
  scanf("%d",&n);
  int b[n],k=-1,j,c,res=0,flag=0;
  while(n)
  {
    k=k+1;
    b[k]=n%2;
    if(n%2==0)
    {
      flag=1;  
    }
    //printf("%d",b[k]);
    n=n/2;
  }
  if(flag==0)
  {
      k++;
      b[k]=1;
  }
  j=k;
  while(j>=0&&b[j]==1)
  {
      j--;
  }
b[j]=1;
j=k;
while(j>=0)
{
    res=res+b[j]*pow(2,c);
    j--;
    c++;
}
printf("%d",res);*/
int n,i;
scanf("%d",&n);
scanf("%d",&i);
int b[n],k=-1;
while(n>0)
{
    k++;
    b[k]=n%2;
   // printf("%d",b[k]);
    n=n/2;
}
if(b[i])
{
    printf("Yes");
}
else 
{
    printf("No");
}
    return 0;
    
}
