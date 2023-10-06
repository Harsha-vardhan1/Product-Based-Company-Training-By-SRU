l=list(map(int,input().split()))
def  merge(first,mid,last):
    print(l[first:mid])
    print(l[mid:last+1])
    i=first
    j=mid
    b=[]
    for m in range(0,first+last+1):
        if i<mid and j<=last and  l[i]<l[j] :
            b.append(l[i])
            i+=1
        elif j<=last:
            b.append(l[j])
            j+=1
        else:
            b.append(l[i])
            i+=1
    i=first
    for k in b:
        l[i]=k
        i+=1
    '''k=-1
    b=[]
    i=first
    j=mid+1
    while i<mid or j<=last:
        if i<mid and j<=last and l[i]<l[j]:
            k+=1
            b.append(l[i])
        elif i<mid and j<=last and l[j]<l[i]:
            k+=1
            b.append(l[j])
            j+=1
        elif i<mid:
            k+=1
            b.append(l[i])
            i+=1
        elif j<=last:
            k+=1
            b.append(l[j])
            j+=1
    i=first
    m=0
    while(i<=last):
        l[i]=b[m]
        m+=1
    '''
def divide(first,last):
    if first<last:
     mid=(first+last)//2
     divide(first,mid)
     divide(mid+1,last)
     if first!=last:
      i=first
      j=mid+1
      b=[]
      for m in range(0,last-first+1):
         if i!=mid+1 and j<=last and l[i]<=l[j]:
             b.append(l[i])
             i+=1
         elif i!=mid+1 and j<=last and l[i]>l[j]:
             b.append(l[j])
             j+=1
         elif i!=mid+1:
             b.append(l[i])
             i+=1
         elif j!=mid+1:
             b.append(l[j])
             j+=1
      i=first
      for c in b:
         l[i]=c
         i+=1
divide(0,len(l)-1)
print(l)
    