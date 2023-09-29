'''Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.'''
#power of 2
n=int(input())
s=""
s+=bin(n)
if(s[2]=='1' and s.count('1')==1):
    print(True)
else:
    print(False)
#power of 4
n=int(input())
s=""
s+=bin(n)
if((s.count('0')-1)%2==0 and s.count('1')==1):
  print(True)
else:
    print(False)