t=int(input())
for _ in range(t):
    n = int(input())
    a =list(map(int,input().split()))
    ind=[0]*(n+1)
    ans=[0]*(n+1)
    ans[1]=0
    ind[a[0]]=1
    for i in range(2,n+1):
        if(ind[a[i-1]]==0):
            ind[a[i-1]]=i
            ans[i]=ans[i-1]
        else:
            ans[i]=max(ans[i-1],i-ind[a[i-1]]+ans[ind[a[i-1]]],i-ind[a[i-1]]+1+ans[ind[a[i-1]]-1])
            ind[a[i-1]]=i
    print(ans[n])

    
    '''ind=[0]*(n+1)
    ind[a[0]]+=1
    for j in range(2,n+1):
        if(ind[a[j-1]]==0):
            ans[j]=ans[j-1]
            ind[a[j-1]]+=1
        else:
            ans[j]=max(ans[j-1],d[a[j-1]][ind[a[j-1]]]-d[a[j-1]][ind[a[j-1]]-1]+1+ans[d[a[j-1]][ind[a[j-1]]-1]-1],d[a[j-1]][ind[a[j-1]]]-d[a[j-1]][ind[a[j-1]]-1]+ans[d[a[j-1]][ind[a[j-1]]-1]])
            ind[a[j-1]]+=1
    print(ans[n])'''
