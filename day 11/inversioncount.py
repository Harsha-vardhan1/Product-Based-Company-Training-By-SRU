l=list(map(int,input().split()))
res=0
l=list(map(int,input().split()))
res=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            res+=1 
print(res)