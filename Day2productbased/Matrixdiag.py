'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
l=[]
n=int(input())
for i in range(0,n):
    m=[]
    for j in range(0,n):
        d=int(input())
        m.append(d)
    l.append(m)
print(l)
a1_v_c=0
a1_h_c=0
a1_d_c=0
a1_rd_c=0
a0_v_c=0
a0_h_c=0
a0_d_c=0
a0_rd_c=0
for m in l:
    if 0 not in m:
        a1_h_c+=1
    elif 1 not in m:
        a0_h_c+=1
for j in range(0,n):
 m=[]
 for i in range(0,n):
   m.append(l[i][j])
 if 0 not in m:
     a1_v_c+=1
 elif 1 not in m:
     a0_v_c+=1 
m=[]
for i in range(0,n):
    m.append(l[i][i])
if 0 not in m:
     a1_d_c+=1
elif 1 not in m:
     a0_d_c+=1 
m=[]
for i in range(0,n):
    for j in range(0,n):
        if i+j>=n-1:
            m.append(l[i][j])
if 0 not in m:
     a1_rd_c+=1
elif 1 not in m:
     a0_rd_c+=1 
print(a1_h_c)
print(a1_v_c)
print(a1_d_c)
print(a1_rd_c)
print(a0_h_c)
print(a0_v_c)
print(a0_d_c)
print(a0_rd_c)


    
    

        
