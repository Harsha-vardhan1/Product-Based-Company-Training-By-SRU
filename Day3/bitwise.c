/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
  /*long a=-1000,t=a;
   int res=0,c=0;
  while(a)
  {
      if(a%2==1)
      {
          res+=1;
      }
      printf("%ld",a%2);
      c=c+1;
      a=a/2;
  }
 
  {  printf(" %d",res);}
  else
  {
      printf(" %d",c-res);
  }*/
  long long int a=-1,count=0;
  while(a)
  {
      count++;
      printf("%lld",a&(a-1));
      a=a&(a-1);
  }
  printf("%lld",count);
  /*int res=0;
  while(a)
  {
      if(a&1)
      {
          res++;
      }
      a=a>>1;
  }
  printf("%d",res);*/
return 0;
}
